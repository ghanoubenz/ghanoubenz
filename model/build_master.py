#!/usr/bin/env python3
"""Build data/opportunities_master.csv from the four Phase 2 opportunity files.

All judgement inputs (volumes, family profiles, evidence overrides, longlist price
fallbacks) are explicit dictionaries below so the scoring can be audited/changed.
"""
import csv, re, math

D = '/home/user/ghanoubenz/data/'
FILES = ['phase2_closures_opportunities.csv', 'phase2_joinery_construction_opportunities.csv',
         'phase2_irrigation_furniture_opportunities.csv', 'phase2_other_sectors_opportunities.csv']
OUT = D + 'opportunities_master.csv'

COLS = ('product_id,product,family,sector,machine_fit,material,part_weight_g,cavities,cycle_s,mold_cost_usd,'
        'price_dzd,price_basis,annual_volume_pcs,volume_basis,clamp_t,shot_g,min_press_t,evidence_strength,'
        'pain_summary,known_buyers,s_demand,s_shortage,s_import_dep,s_local_comp,s_cust_conc,s_recurring,s_margin,'
        's_switching,s_custom_b2b,s_mold_afford,s_machine_compat,s_resin_avail,s_tech,s_regulatory,s_quality_risk,'
        's_copy_risk,s_payment_risk,s_wc,s_speed,s_sku_family,s_utilization,hard_kill,kill_reason,'
        'researcher_verdict,next_validation_action').split(',')
assert len(COLS) == 45

rows = {}
order = []
for f in FILES:
    for r in csv.DictReader(open(D + f, encoding='utf-8')):
        rows[r['product_id']] = r
        order.append(r['product_id'])
assert len(order) == 237, len(order)

# ---------------------------------------------------------------- merges (obvious cross-file duplicates)
MERGES = {  # primary : [absorbed]
    'JC-36': ['OS-001'],   # pipe/conduit snap clip (collier atlas) == IRL conduit saddle clip; JC note flags overlap
    'IF-40': ['JC-12'],    # square/rect tube end insert == alu/PVC profile & tube end caps; JC note flags overlap
    'IF-44': ['OS-032'],   # levelling foot M8/M10 (furniture) == appliance levelling foot M8/M10
}
absorbed = {a for v in MERGES.values() for a in v}

# ---------------------------------------------------------------- helpers
NUM = re.compile(r'-?\d[\d,]*\.?\d*')

def nums(s):
    out = []
    for m in NUM.findall(s or ''):
        m = m.replace(',', '')
        try:
            out.append(float(m))
        except ValueError:
            pass
    return out

def first_num(s, default=None):
    n = nums(s)
    return n[0] if n else default

def mid_range(s, default=0.0):
    """Midpoint of a leading 'a-b' range, else first number."""
    s = (s or '').strip()
    m = re.match(r'^[~]?\s*(\d[\d,]*\.?\d*)\s*[-–]\s*(\d[\d,]*\.?\d*)', s)
    if m:
        a, b = float(m.group(1).replace(',', '')), float(m.group(2).replace(',', ''))
        return (a + b) / 2
    v = first_num(s)
    return v if v is not None else default

DENS = [('PA66-UV', 1.14), ('PA-GF30', 1.36), ('PA6-GF', 1.36), ('PP-GF', 1.12), ('PA66', 1.14), ('PA6', 1.13),
        ('POM', 1.41), ('PBT', 1.31), ('ABS', 1.05), ('ASA', 1.07), ('PC', 1.20), ('TPU', 1.20), ('TPE', 1.00),
        ('PVC', 1.40), ('PS', 1.05), ('EPDM', 1.20), ('LDPE', 0.92), ('HDPE', 0.95), ('rPP', 0.92), ('PP', 0.90),
        ('PE', 0.94)]

def density(mat):
    for k, d in DENS:
        if re.search(r'(?<![A-Za-z])' + re.escape(k) + r'(?![A-Za-z0-9])', mat or ''):
            return d
    return 0.90

PRESSES = [60, 80, 100, 120, 160]
SHOT = {60: (20, 90), 80: (30, 135), 100: (35, 160), 120: (45, 200), 160: (60, 280)}
TIE = {60: 310, 80: 360, 100: 380, 120: 410, 160: 470}

def min_press(clamp, shot_eq, width, cav):
    """Return (press, note, raised_cav)."""
    if not clamp or not shot_eq:
        return 999, '', cav
    for P in PRESSES:
        if width and width > TIE[P]:
            continue
        lo, hi = SHOT[P]
        if clamp > 0.85 * P or shot_eq > hi:
            continue
        if shot_eq >= lo:
            return P, '', cav
        if cav:
            newcav = math.ceil(cav * lo / shot_eq)
            k = newcav / cav
            if clamp * k <= 0.85 * P and shot_eq * k <= hi:
                return P, f'cavities raised {int(cav)}->{newcav} to reach {lo} g min shot on {P} t', newcav
    # fallback: clamp and tie-bar fit, shot below press minimum (needs small screw)
    for P in PRESSES:
        if (not width or width <= TIE[P]) and clamp <= 0.85 * P and shot_eq <= SHOT[P][1]:
            return P, f'shot {shot_eq:.0f} g PP-eq below {SHOT[P][0]} g min on {P} t: small screw or more cavities (clamp-limited)', cav
    return 999, '', cav

# ---------------------------------------------------------------- price cascade inputs
FX = 133 * 1.45  # landed import benchmark multiplier on FOB USD
# FOB USD point used per row (median stated by researcher, else range midpoint, else FOB implied by researcher's own
# FOB-based potential price). Only where an FOB was actually found in the research.
FOB = {'CL-001': .02, 'CL-002': .025, 'CL-003': .025, 'CL-005': .035, 'CL-006': .035, 'CL-007': .015, 'CL-008': .02,
       'CL-009': .03, 'CL-010': .06, 'CL-011': .03, 'CL-012': .11, 'CL-023': .07, 'CL-025': .115,
       'JC-01': .030, 'JC-03': .020, 'JC-06': 1.50, 'JC-27': .060, 'JC-30': .080,
       'IF-17': .01, 'IF-28': .31}
# Observed Algerian retail price DZD/pc (x0.55 -> ex-works); label per retail confidence
RETAIL = {'JC-24': (13.6, 'STRONG SIGNAL'), 'JC-25': (5.6, 'STRONG SIGNAL'), 'JC-26': (21.85, 'STRONG SIGNAL'),
          'JC-33': (0.5, 'WEAK SIGNAL'),   # VERIFIED snippet but item attribution uncertain
          'JC-34': (7.8, 'STRONG SIGNAL'), 'JC-35': (8.9, 'STRONG SIGNAL'), 'JC-36': (10.2, 'WEAK SIGNAL'),
          'OS-004': (2.5, 'WEAK SIGNAL'), 'OS-007': (4.5, 'STRONG SIGNAL'), 'OS-009': (15.0, 'WEAK SIGNAL'),
          'OS-010': (55.0, 'WEAK SIGNAL'), 'OS-011': (42.5, 'WEAK SIGNAL')}
# Phase-1 longlist researcher retail/distributor estimates (DZD/pc) for rows with no Phase-2 price; x0.55 ex-works.
# (value, longlist item)
LONGLIST = {
    'CL-004': (16.5, '#58 flip-top 8-25'), 'CL-013': (9, '#63 dropper tips 3-15'), 'CL-017': (25, '#59 overcaps 10-40'),
    'CL-021': (16.5, '#58 flip-top 8-25'), 'CL-027': (3, '#57 PCO caps 2-4'), 'CL-030': (25, '#59 overcaps 10-40'),
    'JC-04': (10, '#29 alu accessories 10-80 (low end, <10 g)'), 'JC-05': (10, '#29 low end'),
    'JC-07': (50, '#30 shutter parts 50-500 (low end, <10 g)'), 'JC-08': (275, '#30 shutter parts midpoint'),
    'JC-09': (275, '#30 shutter parts midpoint'), 'JC-10': (50, '#30 low end'), 'JC-11': (50, '#30 low end'),
    'JC-13': (10, '#29 low end'), 'JC-14': (10, '#29 low end'), 'JC-15': (10, '#29 low end'),
    'JC-16': (20, '#31 fly-screen corners 10-30'), 'JC-18': (45, '#29 midpoint'), 'JC-19': (10, '#29 low end'),
    'JC-20': (10, '#29 low end (corner keys)'), 'JC-23': (10, '#29 low end'), 'JC-28': (40, '#23 continuous spacers 20-60'),
    'JC-29': (19, '#21 spacer wheels 8-30'), 'JC-32': (20, '#24 cones/spacer tubes 10-30'),
    'JC-37': (2.5, '#10 wall plugs 100-400/100'), 'JC-38': (27.5, '#11 insulation anchors 15-40'),
    'OS-002': (25, '#8 conduit fittings 10-40'), 'OS-003': (25, '#8 conduit fittings 10-40'),
    'OS-005': (2, '#9 clips with nail 100-300/100'), 'OS-008': (2.5, '#10 wall plugs 100-400/100'),
    'OS-014': (40, '#17 trunking accessories 20-60'), 'OS-015': (40, '#17'), 'OS-016': (40, '#17'),
    'OS-019': (90, '#15 terminal block 30-150'), 'OS-020': (250, '#4 junction box 150-350'),
    'OS-021': (425, '#5 junction box 250-600'), 'OS-022': (45, '#2 flush box 30-60'),
    'OS-023': (2600, '#16 DB enclosure 1200-4000'), 'OS-027': (80, '#14 lamp holder 40-120'),
    'OS-030': (325, '#85 cooker knob spare 150-500'), 'OS-033': (125, '#88 appliance feet 50-200'),
    'OS-034': (1900, '#87 fridge parts 800-3000'), 'OS-035': (800, '#87 low end (trim)'),
    'OS-037': (1000, '#86 WM filter caps 500-1500'), 'OS-038': (1000, '#86'),
    'OS-039': (50, '#89 AC drain fittings 50-300 (low end, small part)'), 'OS-040': (50, '#89 low end'),
    'OS-041': (175, '#89 midpoint'), 'OS-042': (175, '#89 midpoint'), 'OS-043': (200, '#90 AC pads 100-300'),
    'OS-048': (200, '#91 grilles 200-800 (low end, small)'), 'OS-049': (500, '#91 midpoint'),
    'OS-050': (1650, '#93 filter housings 800-2500'), 'OS-051': (5, '#106 caps & plugs 5-500 (low end, <10 g)'),
    'OS-052': (5, '#106 low end'), 'OS-053': (5, '#106 low end'), 'OS-073': (5, '#106 low end'),
    'OS-054': (252.5, '#106 midpoint (50-200 g)'), 'OS-068': (252.5, '#106 midpoint'), 'OS-072': (252.5, '#106 midpoint'),
    'OS-069': (500, '#106 high end (>200 g)'), 'OS-112': (500, '#106 high end'),
    'OS-055': (100, '#107 knobs 100-600 (low end, small)'), 'OS-096': (100, '#107 low end'),
    'OS-056': (350, '#107 midpoint'), 'OS-057': (350, '#107 midpoint'), 'OS-066': (30, '#95 push clips 10-50'),
    'OS-075': (20, '#102 PV clips 10-30'), 'OS-080': (20, '#102'), 'OS-081': (3.75, '#1 cable ties 150-600/100'),
    'OS-078': (30, '#95'), 'OS-082': (30, '#95'), 'OS-084': (25, '#97 grommets/blanking plugs 10-40'),
    'OS-085': (250, '#100 reservoir caps 100-400'), 'OS-086': (250, '#100'), 'OS-087': (650, '#98 plate frames 300-1000'),
    'OS-088': (250, '#99 wheel caps 100-400'), 'OS-090': (700, '#101 mud flaps 800-2000/pair'),
    'OS-101': (85, '#110 stationery 20-150'), 'OS-102': (85, '#110'), 'OS-103': (85, '#110'), 'OS-104': (85, '#110'),
    'OS-107': (175, '#111 hospital disposables 50-300'), 'OS-108': (175, '#111'), 'OS-109': (175, '#111'),
}

# ---------------------------------------------------------------- annual volume (yr-2, conservative, buyer set only)
VOL = {
 'CL-001':400000,'CL-002':400000,'CL-003':150000,'CL-004':100000,'CL-005':200000,'CL-006':200000,'CL-007':300000,
 'CL-008':300000,'CL-009':150000,'CL-010':100000,'CL-011':200000,'CL-012':60000,'CL-013':300000,'CL-014':100000,
 'CL-015':80000,'CL-016':50000,'CL-017':100000,'CL-018':100000,'CL-019':100000,'CL-020':80000,'CL-021':200000,
 'CL-022':100000,'CL-023':300000,'CL-024':100000,'CL-025':100000,'CL-026':100000,'CL-027':2000000,'CL-028':100000,
 'CL-029':100000,'CL-030':100000,
 'JC-01':300000,'JC-02':200000,'JC-03':200000,'JC-04':100000,'JC-05':20000,'JC-06':10000,'JC-07':20000,'JC-08':10000,
 'JC-09':10000,'JC-10':20000,'JC-11':30000,'JC-13':300000,'JC-14':100000,'JC-15':100000,'JC-16':100000,'JC-17':100000,
 'JC-18':50000,'JC-19':200000,'JC-20':100000,'JC-21':50000,'JC-22':20000,'JC-23':50000,'JC-24':500000,'JC-25':500000,
 'JC-26':300000,'JC-27':100000,'JC-28':50000,'JC-29':100000,'JC-30':200000,'JC-31':100000,'JC-32':100000,
 'JC-33':2000000,'JC-34':500000,'JC-35':100000,'JC-36':500000,'JC-37':100000,'JC-38':50000,'JC-39':30000,'JC-40':300000,
 'IF-01':300000,'IF-02':300000,'IF-03':100000,'IF-04':200000,'IF-05':150000,'IF-06':150000,'IF-07':200000,'IF-08':300000,
 'IF-09':50000,'IF-10':50000,'IF-11':300000,'IF-12':500000,'IF-13':200000,'IF-14':2000000,'IF-15':5000,'IF-16':100000,
 'IF-17':300000,'IF-18':50000,'IF-19':10000,'IF-20':50000,'IF-21':15000,'IF-22':8000,'IF-23':5000,'IF-24':2000,
 'IF-25':200000,'IF-26':300000,'IF-27':100000,'IF-28':50000,'IF-29':50000,'IF-30':30000,'IF-31':10000,'IF-32':5000,
 'IF-33':3000,'IF-34':10000,'IF-35':10000,'IF-36':3000,'IF-37':50000,'IF-38':20000,'IF-39':300000,'IF-40':300000,
 'IF-41':200000,'IF-42':300000,'IF-43':50000,'IF-44':100000,'IF-45':30000,'IF-46':500000,'IF-47':500000,'IF-48':500000,
 'IF-49':100000,'IF-50':20000,'IF-51':100000,'IF-52':50000,'IF-53':20000,'IF-54':10000,'IF-55':5000,
 'OS-002':200000,'OS-003':50000,'OS-004':500000,'OS-005':300000,'OS-006':50000,'OS-007':1000000,'OS-008':1000000,
 'OS-009':200000,'OS-010':100000,'OS-011':50000,'OS-012':50000,'OS-013':100000,'OS-014':50000,'OS-015':50000,
 'OS-016':20000,'OS-017':200000,'OS-018':20000,'OS-019':50000,'OS-020':30000,'OS-021':20000,'OS-022':200000,
 'OS-023':5000,'OS-024':20000,'OS-025':50000,'OS-026':20000,'OS-027':50000,'OS-028':50000,'OS-029':100000,
 'OS-030':10000,'OS-031':10000,'OS-033':20000,'OS-034':10000,'OS-035':10000,'OS-036':20000,'OS-037':10000,
 'OS-038':5000,'OS-039':200000,'OS-040':30000,'OS-041':20000,'OS-042':30000,'OS-043':10000,'OS-044':50000,
 'OS-045':20000,'OS-046':300000,'OS-047':500000,'OS-048':20000,'OS-049':10000,'OS-050':5000,'OS-051':200000,
 'OS-052':200000,'OS-053':200000,'OS-054':10000,'OS-055':10000,'OS-056':2000,'OS-057':5000,'OS-058':5000,
 'OS-059':5000,'OS-060':10000,'OS-061':100000,'OS-062':10000,'OS-063':5000,'OS-064':10000,'OS-065':20000,
 'OS-066':200000,'OS-067':20000,'OS-068':10000,'OS-069':20000,'OS-070':5000,'OS-071':5000,'OS-072':5000,
 'OS-073':20000,'OS-074':5000,'OS-075':50000,'OS-076':50000,'OS-077':20000,'OS-078':200000,'OS-079':20000,
 'OS-080':50000,'OS-081':100000,'OS-082':100000,'OS-083':100000,'OS-084':100000,'OS-085':10000,'OS-086':10000,
 'OS-087':10000,'OS-088':10000,'OS-089':100000,'OS-090':5000,'OS-091':2000,'OS-092':2000,'OS-093':10000,'OS-094':500,
 'OS-095':5000,'OS-096':2000,'OS-097':2000,'OS-098':5000,'OS-099':5000,'OS-100':2000,'OS-101':50000,'OS-102':50000,
 'OS-103':30000,'OS-104':50000,'OS-105':200000,'OS-106':50000,'OS-107':50000,'OS-108':10000,'OS-109':5000,
 'OS-110':200000,'OS-111':20000,'OS-112':20000}
VOL_WEAK = {'JC-01', 'JC-02', 'JC-13', 'JC-19', 'OS-025', 'OS-026', 'OS-039', 'OS-046', 'OS-047', 'OS-069', 'OS-112'}

# ---------------------------------------------------------------- family profiles
# (demand, shortage, import_dep, local_comp, recurring, payment, speed, sku_family, custom_b2b)
PROF = {}
def prof(ids, t):
    for i in ids.split():
        PROF[i] = t
prof('CL-001 CL-002', (6, 5, 7, 5, 9, 6, 6, 7, 3))
prof('CL-005 CL-006', (5, 5, 7, 5, 9, 6, 5, 7, 3))
prof('CL-009 CL-018 CL-021', (4, 4, 6, 5, 9, 6, 5, 6, 3))
prof('CL-003', (5, 4, 7, 5, 9, 6, 6, 8, 6))
prof('CL-004', (4, 5, 6, 5, 8, 6, 4, 2, 9))
prof('CL-007', (6, 2, 4, 3, 9, 6, 7, 6, 3))
prof('CL-008', (6, 2, 4, 3, 9, 6, 7, 5, 5))
prof('CL-010', (4, 4, 5, 5, 9, 7, 3, 3, 7))
prof('CL-011', (5, 2, 3, 3, 9, 6, 6, 4, 5))
prof('CL-012', (4, 4, 5, 5, 9, 6, 5, 4, 7))
prof('CL-013', (4, 4, 5, 3, 9, 6, 6, 5, 6))
prof('CL-014 CL-015 CL-016', (4, 4, 6, 5, 8, 6, 6, 5, 5))
prof('CL-017 CL-019 CL-020 CL-022 CL-030', (3, 4, 6, 5, 8, 6, 5, 3, 5))
prof('CL-023 CL-024 CL-025 CL-026', (7, 5, 8, 6, 9, 6, 1, 4, 2))
prof('CL-027', (8, 0, 1, 0, 9, 7, 2, 2, 1))
prof('CL-028 CL-029', (7, 2, 3, 2, 9, 6, 1, 3, 3))
prof('JC-01 JC-03', (6, 4, 7, 7, 8, 6, 7, 8, 5))
prof('JC-02', (5, 4, 7, 7, 8, 6, 5, 7, 7))
prof('JC-13', (6, 4, 7, 7, 8, 6, 7, 6, 5))
prof('JC-16 JC-17', (5, 4, 7, 7, 7, 6, 7, 6, 5))
prof('JC-04 JC-05 JC-07 JC-08 JC-09 JC-10 JC-11', (4, 4, 7, 7, 7, 6, 5, 7, 7))
prof('JC-06', (4, 4, 7, 6, 7, 6, 3, 5, 7))
prof('JC-14 JC-18', (5, 4, 7, 4, 8, 6, 4, 4, 7))
prof('JC-15', (5, 4, 7, 6, 8, 6, 5, 6, 7))
prof('JC-19', (5, 4, 6, 5, 8, 7, 4, 6, 7))
prof('JC-20', (4, 4, 6, 5, 8, 6, 5, 6, 7))
prof('JC-21 JC-22 JC-28 JC-32', (5, 3, 4, 4, 8, 6, 1, 3, 3))
prof('JC-23', (3, 4, 7, 6, 8, 6, 5, 5, 6))
prof('JC-24 JC-25 JC-26 JC-40', (8, 2, 6, 5, 9, 6, 8, 9, 5))
prof('JC-27', (5, 3, 6, 5, 9, 6, 7, 8, 5))
prof('JC-29 JC-39', (4, 4, 5, 5, 8, 4, 4, 3, 9))
prof('JC-30', (5, 4, 7, 6, 8, 4, 6, 5, 5))
prof('JC-31', (3, 4, 7, 6, 8, 4, 6, 4, 4))
prof('JC-33', (7, 1, 4, 4, 9, 6, 7, 6, 2))
prof('JC-34', (7, 2, 7, 6, 9, 6, 8, 6, 2))
prof('JC-35', (4, 2, 7, 6, 5, 6, 7, 4, 2))
prof('JC-36', (7, 3, 5, 4, 9, 6, 8, 8, 3))
prof('JC-37', (5, 4, 7, 6, 8, 6, 4, 3, 2))
prof('JC-38', (3, 4, 6, 5, 7, 5, 5, 6, 5))
prof('IF-01 IF-02 IF-03 IF-04 IF-05 IF-06 IF-07 IF-08 IF-20', (7, 4, 7, 4, 7, 5, 6, 8, 3))
prof('IF-09 IF-10', (6, 4, 7, 4, 7, 5, 4, 6, 3))
prof('IF-11', (5, 4, 7, 4, 7, 5, 1, 5, 3))
prof('IF-12 IF-13', (7, 4, 7, 4, 8, 5, 1, 5, 2))
prof('IF-14', (6, 4, 7, 4, 8, 5, 1, 3, 4))
prof('IF-15', (3, 4, 7, 4, 4, 5, 6, 2, 2))
prof('IF-16 IF-17', (5, 4, 7, 4, 7, 5, 6, 6, 2))
prof('IF-18 IF-19', (4, 4, 6, 4, 6, 5, 4, 4, 3))
prof('IF-21 IF-22', (5, 4, 6, 3, 7, 5, 3, 6, 3))
prof('IF-23 IF-24', (4, 4, 6, 4, 5, 5, 2, 3, 3))
prof('IF-25 IF-26 IF-27', (4, 4, 6, 5, 7, 5, 6, 6, 3))
prof('IF-28', (6, 5, 8, 7, 7, 5, 5, 5, 3))
prof('IF-29 IF-30', (5, 5, 8, 7, 7, 5, 6, 5, 4))
prof('IF-31 IF-32 IF-33', (4, 5, 7, 5, 5, 5, 2, 3, 3))
prof('IF-34 IF-35 IF-36', (3, 4, 6, 5, 5, 6, 5, 3, 3))
prof('IF-37', (3, 4, 7, 5, 6, 3, 1, 3, 4))
prof('IF-38', (4, 6, 8, 6, 7, 3, 3, 5, 9))
prof('IF-39 IF-40 IF-41 IF-42', (6, 4, 7, 6, 8, 5, 7, 8, 6))
prof('IF-43 IF-45', (4, 4, 7, 6, 8, 5, 5, 6, 4))
prof('IF-44', (5, 4, 7, 6, 8, 5, 5, 6, 5))
prof('IF-46 IF-47', (5, 4, 7, 6, 8, 5, 7, 8, 5))
prof('IF-48', (5, 4, 7, 6, 8, 5, 7, 4, 3))
prof('IF-49 IF-50', (4, 4, 7, 6, 8, 5, 6, 6, 6))
prof('IF-51 IF-52', (3, 4, 7, 6, 7, 5, 4, 5, 7))
prof('IF-53 IF-54 IF-55', (3, 4, 8, 6, 7, 6, 3, 3, 3))
prof('OS-002', (6, 3, 5, 5, 9, 6, 7, 7, 3))
prof('OS-003', (4, 3, 5, 5, 8, 6, 6, 6, 3))
prof('OS-004 OS-005', (7, 2, 6, 5, 9, 6, 6, 5, 2))
prof('OS-006 OS-007 OS-081', (6, 2, 6, 3, 9, 6, 5, 4, 2))
prof('OS-008', (8, 3, 7, 5, 9, 6, 6, 7, 2))
prof('OS-009', (6, 3, 7, 6, 9, 6, 7, 5, 2))
prof('OS-010', (5, 3, 7, 6, 9, 6, 7, 5, 2))
prof('OS-011 OS-012', (5, 3, 7, 5, 8, 6, 3, 3, 2))
prof('OS-013 OS-017 OS-018 OS-019 OS-029', (3, 3, 6, 5, 8, 6, 5, 5, 3))
prof('OS-014 OS-015 OS-016', (5, 3, 5, 5, 8, 6, 5, 7, 8))
prof('OS-020 OS-021 OS-022 OS-028', (6, 2, 3, 2, 9, 6, 5, 4, 3))
prof('OS-023', (5, 2, 4, 4, 8, 6, 2, 3, 3))
prof('OS-024', (3, 2, 2, 1, 8, 5, 1, 3, 7))
prof('OS-025', (4, 3, 5, 4, 8, 4, 4, 6, 7))
prof('OS-026', (4, 3, 5, 4, 8, 4, 2, 3, 5))
prof('OS-027', (4, 3, 6, 4, 8, 6, 2, 3, 3))
prof('OS-030 OS-031 OS-036 OS-037', (4, 4, 6, 4, 6, 5, 4, 3, 6))
prof('OS-033 OS-035', (4, 4, 6, 4, 6, 5, 4, 3, 6))
prof('OS-034 OS-038', (4, 3, 4, 3, 6, 5, 2, 3, 6))
prof('OS-039 OS-046 OS-047', (6, 4, 7, 5, 8, 6, 4, 4, 5))
prof('OS-040 OS-042 OS-043 OS-044', (5, 4, 6, 5, 7, 6, 6, 5, 4))
prof('OS-041', (5, 4, 6, 5, 7, 6, 1, 3, 3))
prof('OS-045', (3, 4, 6, 5, 6, 2, 3, 3, 6))
prof('OS-048 OS-049 OS-050 OS-099', (4, 3, 6, 5, 6, 6, 5, 4, 3))
prof('OS-051 OS-052 OS-053', (5, 4, 7, 7, 8, 6, 6, 9, 6))
prof('OS-054', (4, 4, 7, 7, 7, 6, 5, 6, 6))
prof('OS-055 OS-056 OS-057 OS-058 OS-096', (3, 4, 7, 6, 5, 6, 5, 6, 5))
prof('OS-059 OS-060', (3, 4, 7, 6, 5, 6, 4, 3, 8))
prof('OS-061 OS-062', (4, 2, 6, 3, 7, 6, 5, 4, 2))
prof('OS-063 OS-065', (3, 3, 6, 4, 6, 5, 5, 3, 3))
prof('OS-064', (3, 4, 6, 5, 4, 6, 5, 2, 10))
prof('OS-066', (5, 4, 7, 5, 8, 6, 6, 6, 4))
prof('OS-067', (3, 4, 6, 6, 7, 4, 4, 3, 6))
prof('OS-068', (4, 4, 8, 8, 8, 4, 3, 4, 8))
prof('OS-069 OS-112', (6, 4, 8, 8, 8, 4, 2, 4, 8))
prof('OS-070 OS-071 OS-074', (4, 4, 7, 6, 7, 4, 1, 3, 6))
prof('OS-072', (2, 4, 7, 6, 7, 4, 3, 3, 6))
prof('OS-073', (4, 6, 7, 6, 7, 6, 3, 8, 6))
prof('OS-075 OS-080', (4, 4, 8, 7, 7, 6, 4, 4, 3))
prof('OS-076 OS-077 OS-079', (3, 3, 7, 6, 6, 6, 5, 3, 5))
prof('OS-078 OS-082 OS-084', (6, 7, 7, 4, 8, 6, 5, 5, 5))
prof('OS-083', (4, 3, 5, 3, 8, 6, 1, 3, 5))
prof('OS-085 OS-086', (3, 6, 6, 4, 6, 6, 4, 3, 5))
prof('OS-087 OS-088 OS-089 OS-090', (3, 4, 5, 4, 6, 6, 4, 3, 3))
prof('OS-091 OS-092 OS-093 OS-094 OS-095 OS-097 OS-100', (3, 4, 6, 4, 5, 6, 4, 3, 7))
prof('OS-098', (5, 6, 8, 6, 6, 6, 3, 3, 10))
prof('OS-101 OS-102 OS-103 OS-104 OS-105 OS-106', (5, 2, 3, 4, 6, 6, 6, 4, 1))
prof('OS-107 OS-108 OS-109 OS-110', (5, 3, 5, 2, 8, 3, 1, 3, 2))
prof('OS-111', (3, 3, 7, 5, 7, 6, 1, 3, 4))

# ---------------------------------------------------------------- evidence strength (strict)
EV2 = {'JC-24', 'JC-25', 'JC-26', 'JC-34', 'JC-35', 'OS-007', 'OS-009', 'OS-010', 'OS-068', 'OS-069', 'OS-112',
       'OS-073', 'OS-098'}
EV0 = set(('CL-016 CL-017 CL-019 CL-028 CL-029 CL-030 JC-05 JC-07 JC-08 JC-09 JC-10 JC-11 JC-17 JC-20 JC-22 JC-31 JC-32 '
           'JC-37 JC-38 IF-25 IF-26 IF-27 IF-33 IF-34 IF-35 IF-36 IF-37 IF-50 IF-51 IF-52 IF-54 IF-55 OS-012 OS-013 '
           'OS-017 OS-019 OS-027 OS-029 OS-040 OS-041 OS-042 OS-043 OS-044 OS-048 OS-049 OS-050 OS-051 OS-052 OS-053 '
           'OS-055 OS-056 OS-057 OS-058 OS-060 OS-062 OS-064 OS-065 OS-066 OS-072 OS-074 OS-081 OS-083 OS-086 OS-087 '
           'OS-088 OS-089 OS-090 OS-091 OS-092 OS-093 OS-094 OS-095 OS-096 OS-097 OS-099 OS-100 OS-101 OS-102 OS-103 '
           'OS-104 OS-105 OS-106 OS-110').split())

# ---------------------------------------------------------------- researcher verdicts for closures (from p2_closures.md s.5)
CL_VERDICT = {
 'CL-001': 'INVESTIGATE (leaning GO)', 'CL-002': 'INVESTIGATE (leaning GO)', 'CL-003': 'INVESTIGATE (leaning GO)',
 'CL-004': 'INVESTIGATE', 'CL-005': 'INVESTIGATE (after flip-top)', 'CL-006': 'INVESTIGATE (after flip-top)',
 'CL-007': 'RANGE FILLER ONLY', 'CL-008': 'RANGE FILLER ONLY', 'CL-009': 'INVESTIGATE (low)', 'CL-010': 'INVESTIGATE',
 'CL-011': 'INVESTIGATE (low)', 'CL-012': 'INVESTIGATE (low)', 'CL-013': 'PARK', 'CL-014': 'INVESTIGATE (later)',
 'CL-015': 'INVESTIGATE (later)', 'CL-016': 'INVESTIGATE (later)', 'CL-017': 'PARK', 'CL-018': 'PARK',
 'CL-019': 'PARK', 'CL-020': 'PARK', 'CL-021': 'PARK', 'CL-022': 'PARK', 'CL-023': 'KILL (phase 1)',
 'CL-024': 'KILL (phase 1)', 'CL-025': 'KILL (phase 1)', 'CL-026': 'KILL (phase 1)', 'CL-027': 'KILL',
 'CL-028': 'KILL (use blowers as channel)', 'CL-029': 'KILL (use blowers as channel)', 'CL-030': 'PARK'}
CL_KILL = {
 'CL-023': 'Other process: 6-10 precision molds + springs/balls + automatic assembly; FOB US$0.04-0.10',
 'CL-024': 'Other process: multi-part foam pump with metal parts and automatic assembly',
 'CL-025': 'Other process: multi-part trigger with metal parts and automatic assembly; FOB US$0.05-0.18',
 'CL-026': 'Other process: multi-part fine-mist pump with metal parts and automatic assembly',
 'CL-027': 'SGT scale: incumbents run 32-72-cavity hot runners on 200-300 t systems; oversupplied',
 'CL-028': 'Blow molding, not injection; blowers are channel partners', 'CL-029': 'Blow molding / PET preform not viable on a 120 t PP press'}

# Concrete replacements for vague next actions
NEXT_OVR = {
 'CL-017': 'Photograph overcaps on 10 pump-packed cosmetics during the closures shelf audit and note origin',
 'CL-018': 'Ask PAFIX and E.C.A Birtouta whether 24/410 turret caps sell and their DZD per 1,000',
 'CL-020': 'Ask Dermal Group whether roll-on caps/ball housings are imported, from whom, and annual volume',
 'CL-013': 'Ask SIPEM for its list and DZD per 1,000 of orifice reducers by neck size',
 'OS-069': 'In the TSS purchasing call, also ask 9-5/8 to 13-3/8 in protector type, origin, price and annual quantity (future-press case)',
 'OS-112': 'In the TSS purchasing call, also ask 6-5/8 to 7 in protector type, origin, price and annual quantity (future-press case)',
 'OS-071': 'Ask Alfapipe what end/bevel protection (if any) it uses on line pipe (future-machine case only)',
}


def _ov(ids, txt):
    for i in ids.split():
        NEXT_OVR[i] = txt
_ov('OS-008 OS-009 OS-010', 'Quote anchors with SOGEDIM, Mabricole, Assly + 2 El Hamiz/El Eulma wholesalers: DZD per 100 and per 1,000 (butterfly, hammer-fix, nylon), monthly volume, origin')
_ov('OS-002 OS-003', 'Ask SOGEDIM + 2 El Eulma electrical wholesalers: DZD per 100, origin and monthly volume of IRL couplers/elbows; check if conduit extruders bundle them')
_ov('OS-013 OS-018 OS-029', 'Ask 3 panel builders (via SOGEDIM/Elecmarket) which small plastics they import, DZD per 100 and annual quantity')
_ov('OS-014 OS-015 OS-016', 'Identify the local trunking (goulotte) extruders; get profile drawings and ask how they source end caps/corners and at what price')
_ov('OS-020 OS-021', 'Price-check HAOUAS vs FAMATEL boxes at SOGEDIM; pursue only as private label for one distributor')
_ov('OS-025', 'Ask ENICAB purchasing for its list, origin and prices of cable end caps and drum consumables (and whether heat-shrink is used instead)')
_ov('OS-030 OS-036 OS-037', 'Ouedkniss spare-part price check, then ask Samha/Geant after-sales which plastic spares are most requested and out of stock')
_ov('OS-039 OS-046 OS-047', 'Call Samha, Geant and Condor-Hisense local-integration managers: which small plastics (feet, clamps, condensate elbows) are still in CKD kits, volumes, target price')
_ov('OS-040 OS-042', 'Ask 3 HVAC distributors/AC installers: origin, DZD price and yearly quantity of wall sleeves/duct accessories; find any local duct extruder')
_ov('OS-048', 'Price-check round ventilation grilles at 3 construction/HVAC distributors (DZD, origin, monthly volume)')
_ov('OS-051 OS-052 OS-053', 'Call 3 hydraulic-hose assemblers / steel-tube makers: caps and plugs used, origin, DZD per 1,000, annual quantity')
_ov('OS-054', 'Ask 2 valve/flange stockists serving Sonatrach which flange protectors they fit, origin and price')
_ov('OS-055 OS-056 OS-057 OS-096', 'Ask 3 machine builders/maintenance shops which knobs/handles they import (Elesa-type), DZD price and yearly quantity')
_ov('OS-058 OS-092', 'Ask 3 bottling/food plants\' maintenance chiefs which guide-rail brackets and machine feet they import, lead time and price')
_ov('OS-064', 'Ask 3 electronics/IoT assemblers (e.g. via CDTA network) for enclosure needs, volumes and willingness to fund a mold')
_ov('OS-066 OS-078 OS-082 OS-084 OS-085', 'Call 3 aftermarket parts wholesalers: which plastic clips/plugs are out of stock, for which fleet models, and DZD prices')
_ov('OS-067', 'Ask Tosyali/Sider packaging departments what coil edge protectors they use (plastic, cardboard, steel) and quantities')
_ov('OS-073', 'Register on the Sonatrach local-supplier list and ask stores for imported plastic dust-cap references and quantities')
_ov('OS-075 OS-080 OS-077 OS-079', 'Ask Zergoun and Aures Solaire which PV clips/corners/rail caps they import, DZD price and annual quantity')
_ov('OS-099', 'Ask 2 water/industrial filter distributors which end caps they import and at what price')
_ov('JC-36', 'Ask SOGEDIM, Assly + 2 El Eulma wholesalers: DZD per 100, origin and monthly volume of 16-32 mm IRL/PER snap clips; check whether HAOUAS-type local molders already make them')
_ov('OS-072', 'Ask TSS whether any Algerian threader handles 2-3/8 to 3-1/2 in tubing; otherwise drop')

GENERIC_NEXT_BAD = re.compile(r'^(none|later|deprioriti[sz]e|low priority|only if|price \+ origin check at 3 distributors)', re.I)

# ---------------------------------------------------------------- mapping helpers
def sc_cust(t):
    t = (t or '').lower()
    if not t or t == 'unknown': return 5
    if 'single' in t: return 1
    if 'very concentrated' in t: return 2
    if ('fragmented' in t or t.startswith('low')) and ('concentrated' in t or 'plant' in t or 'few large' in t): return 6
    if t.startswith('low-medium'): return 7
    if 'fragmented' in t or t.startswith('low'): return 8
    if t.startswith('medium'): return 5
    if any(k in t for k in ('concentrated', 'high', 'few')): return 3
    return 5

def sc_switch(t):
    t = (t or '').lower().strip()
    if not t or t.startswith('unknown'): return 5
    if t.startswith('very high'): return 1
    if t.startswith('medium-high'): return 4
    if t.startswith('low-medium'): return 7
    if t.startswith('high') or t == 'h': return 3
    if t.startswith('medium') or t == 'm': return 5
    if t.startswith('low') or t == 'l': return 8
    return 5

def sc_wc(t, sector, mat):
    t = (t or '').lower()
    if t.startswith('mold ~'):  # irrigation/furniture file: capex text; derive from sector/material
        if 'irrigation' in (sector or '').lower(): return 4
        return 5 if density(mat) > 1.0 else 6
    if not t or t.startswith('unknown'): return 5
    if t.startswith('medium-high'): return 4
    if t.startswith('low for us'): return 6
    if t.startswith('high'): return 2
    if t.startswith('low-med'): return 7
    if t.startswith('low-medium'): return 7
    if t.startswith('med'): return 5
    if t.startswith('low'): return 8
    return 5

def sc_copy(t):
    t = (t or '').lower().strip()
    if not t or t.startswith('unknown') or t.startswith('n/a'): return 5
    if t.startswith('low-medium'): return 6
    if t.startswith('low') or t.startswith('l ') or t == 'l' or t.startswith('l ('): return 8
    if t.startswith('medium') or t == 'm': return 5
    if t.startswith('high') or t.startswith('h'): return 2
    return 5

def sc_quality(t):
    """returns (tech, quality_risk)"""
    t = (t or '').lower().strip()
    if not t or t.startswith('unknown'): return 5, 5
    if t.startswith('very high'): return 1, 1
    if t.startswith('medium-high'): return 4, 4
    if t.startswith('low-medium'): return 8, 7
    if t.startswith('high') or t.startswith('h'): return 3, 3
    if t.startswith('medium') or t.startswith('m'): return 6, 6
    if t.startswith('low') or t.startswith('l'): return 9, 8
    return 5, 5

def sc_reg(t):
    t = (t or '').lower().strip()
    if not t or t.startswith('unknown'): return 5
    if t.startswith('l-m') or t.startswith('low-medium'): return 7
    if t.startswith('m-h') or t.startswith('medium-high'): return 3
    if t.startswith('low') or t.startswith('l'): return 9
    if t.startswith('medium') or t.startswith('m'): return 5
    if t.startswith('high') or t.startswith('h'): return 1
    return 5

def sc_resin(mat):
    m = mat or ''
    if 'steel spring' in m: return 5
    if 'EPDM' in m: return 1
    if re.search(r'\b(POM|ABS|PC|PBT|ASA|TPE|TPU)\b', m): return 2
    if 'PA66-UV' in m: return 3
    if re.search(r'PA', m): return 4
    if 'PP-GF' in m: return 5
    if 'fibre-concrete' in m: return 5
    if 'rPP' in m: return 9
    if 'hinge grade' in m: return 7
    if re.search(r'\b(PS|PVC|PET)\b', m) and not re.search(r'\bPP\b', m): return 7
    if 'clarified' in m: return 7
    if re.search(r'\b(PP|HDPE|LDPE|PE)\b', m): return 8
    return 5

def sc_mold(cost):
    if cost <= 0: return 5
    if cost <= 5000: return 10
    if cost <= 7000: return 9
    if cost <= 9000: return 7
    if cost <= 12000: return 6
    if cost <= 15000: return 4
    if cost <= 20000: return 3
    if cost <= 30000: return 2
    return 1

def sc_margin(m):
    if m is None: return 5
    if m >= .70: return 9
    if m >= .55: return 8
    if m >= .40: return 6
    if m >= .25: return 4
    if m >= .10: return 2
    return 0

def sc_util(h):
    if h >= 2000: return 10
    if h >= 1200: return 8
    if h >= 700: return 6
    if h >= 350: return 4
    if h >= 150: return 3
    if h >= 50: return 2
    return 1

HARD_RESIN = re.compile(r'\b(POM|ABS|PC|PBT|ASA|TPE|TPU)\b')
CERT_KILL = {
 'OS-019': 'Certification: IEC 60947-7-1 / UL94 V0 terminal block',
 'OS-024': 'Utility approval (Sonelgaz) and captive in-house supply (SAIEG)',
 'OS-027': 'Certification: IEC 60238 heat-rated lamp holder',
 'OS-083': 'Automotive OEM: IATF 16949 / PPAP',
 'OS-107': 'Medical: ISO 13485 clean room; MBS PLAST incumbent', 'OS-108': 'Medical: ISO 13485 / regulatory registration',
 'OS-109': 'Medical: ISO 13485 (and blow molding)', 'OS-110': 'Medical: ISO 13485 sterile precision part',
 'OS-111': 'Certification: IEC 62790 / TUV PV junction box',
 'IF-37': 'Official ID approval (ICAR-type numbering, state tender); TPU not stocked',
 'OS-086': 'Safety pressure-valve assembly (spring/valve) on coolant circuit',
 'CL-027': 'Commodity scale incumbent (SGT ~2 bn caps/yr, 32-72-cav hot runners)',
 'IF-12': 'Emitter precision / ISO 9261 flow testing', 'IF-13': 'Emitter precision (PC membrane) / ISO 9261',
 'IF-14': 'Emitter micron precision tied to extruder inserter / ISO 9261',
 'JC-33': 'Retail 0.5 DZD/pc below plausible cost + margin (~0.1 DZD/pc absolute)',
 'JC-35': 'Retail 6.8-11 DZD gives negative margin at ex-works price',
 'OS-004': 'Retail 2-3 DZD/pc below cost once steel nail + manual insertion are added',
 'OS-005': 'Retail ~2-3 DZD/pc below cost once steel nail + manual insertion are added',
 'OS-011': 'TPE seal insert not stocked locally; 12-18 unscrewing tools vs 35-50 DZD retail imports',
}

JC_VERDICT = {
 'JC-01': 'GO-candidate (gate: Hammedi visit)', 'JC-02': 'INVESTIGATE (after JC-01)', 'JC-03': 'GO-candidate (bundle with JC-01)',
 'JC-04': 'INVESTIGATE (shutter kit)', 'JC-05': 'INVESTIGATE (shutter kit)', 'JC-06': 'KILL', 'JC-07': 'INVESTIGATE (shutter kit)',
 'JC-08': 'INVESTIGATE (shutter kit)', 'JC-09': 'KILL (low)', 'JC-10': 'INVESTIGATE (shutter kit)', 'JC-11': 'INVESTIGATE (shutter kit)',
 'JC-12': 'INVESTIGATE', 'JC-13': 'GO-candidate', 'JC-14': 'KILL', 'JC-15': 'INVESTIGATE', 'JC-16': 'GO-candidate (if 1-2 profiles dominate)',
 'JC-17': 'GO-candidate (bundle with JC-16)', 'JC-18': 'KILL', 'JC-19': 'INVESTIGATE (Izdihar integration)', 'JC-20': 'INVESTIGATE',
 'JC-21': 'KILL', 'JC-22': 'KILL', 'JC-23': 'KILL (low)', 'JC-24': 'GO (gate: 3 wholesaler calls)', 'JC-25': 'GO (gate: 3 wholesaler calls)',
 'JC-26': 'GO (gate: 3 wholesaler calls; lead SKU)', 'JC-27': 'INVESTIGATE', 'JC-28': 'KILL', 'JC-29': 'INVESTIGATE (needs named buyer)',
 'JC-30': 'INVESTIGATE (GO if tube+cone system common)', 'JC-31': 'INVESTIGATE', 'JC-32': 'KILL', 'JC-33': 'KILL',
 'JC-34': 'GO (gate: 3 tile-shop calls)', 'JC-35': 'KILL stand-alone (kit companion only)', 'JC-36': 'INVESTIGATE', 'JC-37': 'KILL (for start)',
 'JC-38': 'INVESTIGATE (low)', 'JC-39': 'INVESTIGATE (via plant interview)', 'JC-40': 'INVESTIGATE (3rd spacer SKU)'}
REASON_OVR = {
 'JC-35': 'Negative margin at 50% of lowest retail (6.8 DA); ~14% at 11 DA; do not tool alone, only as tile-clip kit companion',
 'JC-06': 'Needs ~207 t (2-cav ASA, ~150 cm2 each); many cheeks are aluminium anyway',
 'OS-041': 'Extrusion product (future machine); its injection accessories are OS-042',
 'OS-109': 'Blow molding (future machine); medical regulatory barrier',
 'IF-23': 'Machine size: shot >200 g / mold 450 mm (needs >120 t press)', 'IF-24': 'Machine size: clamp ~250 t, shot ~1 kg, mold 600 mm',
 'IF-31': 'Machine size: clamp ~330 t, shot ~520 g', 'IF-32': 'Machine size: clamp ~190 t, shot ~290 g',
 'IF-33': 'Machine size: clamp ~370 t, mold 600 mm', 'IF-36': 'Machine size: projected area needs >800 t',
 'IF-55': 'Machine size: 5-star base needs ~1,000 t press',
}

def verdict_and_reason(pid, r):
    sn = (r['stage_notes'] or '').strip()
    if pid.startswith('CL-'):
        v = CL_VERDICT[pid]
        reason = CL_KILL.get(pid, '')
        return v, reason
    if pid.startswith('IF-'):
        m = re.match(r'VERDICT\s+([^.]*)\.', sn)
        v = m.group(1).strip() if m else ''
        reason = ''
        if v.upper().startswith('KILL'):
            reason = re.sub(r'^KILL\s*', '', v).strip(' ()') or 'Researcher KILL'
            # enrich from note
            extra = {'IF-11': 'EPDM needs rubber molding (TPE trial only if buyers accept)',
                     'IF-12': 'Precision labyrinth, ISO 9261 testing, brand trust (Aster, Irritec, Caudal)',
                     'IF-13': 'PC membrane emitter: ISO 9261, brand trust, US$30k mold, ~10% margin',
                     'IF-14': 'Inline emitter: micron tolerances, tied to extruder inserter, US$45k mold'}
            reason = extra.get(pid, REASON_OVR.get(pid, reason))
        return v, reason
    if pid.startswith('JC-'):
        v = JC_VERDICT[pid]
        reason = ''
        if v.upper().startswith('KILL'):
            sn2 = re.split(r'CALC:', sn)[0].strip()
            reason = REASON_OVR.get(pid) or re.sub(r'^(KILL[^:]*:\s*)', '', sn2).strip()
        return v, reason
    # OS: verdict = text before ':' or CALC
    head = re.split(r'CALC:', sn)[0].strip()
    head_nofit = re.split(r'\[Fit note', head)[0].strip()
    m = re.match(r'^([A-Za-z/ \-]+?(?:\([^)]*\))?)(?:[:.;]|$)\s*(.*)$', head_nofit)
    if m:
        v = m.group(1).strip()
        rest = m.group(2).strip()
    else:
        v, rest = head_nofit, ''
    v = v.strip()
    reason = ''
    if re.search(r'KILL|FUTURE', v, re.I):
        reason = rest if rest else head_nofit
        if pid.startswith('JC-') and not rest:
            reason = head_nofit
        reason = reason.strip()
        if re.search(r'FUTURE', v, re.I) and not reason.lower().startswith('future'):
            reason = 'Future machine: ' + reason
    reason = REASON_OVR.get(pid, reason)
    return v, reason

def short(s, n=260):
    s = re.sub(r'\s+', ' ', (s or '').strip())
    return s if len(s) <= n else s[:n - 3].rstrip() + '...'

# ---------------------------------------------------------------- build
out = []
for pid in order:
    if pid in absorbed:
        continue
    r = rows[pid]
    merged = MERGES.get(pid, [])
    mrows = [rows[m] for m in merged]
    sector = r['sector']; mat = r['material']; fit = r['machine_fit'].strip()

    # numerics
    pw = r['part_weight_g']
    if pid == 'CL-023': pw_v = 7.0
    elif pid in ('CL-024', 'CL-025', 'CL-026'): pw_v = mid_range(pw.lstrip('~'))
    else: pw_v = mid_range(pw) if nums(pw) else 0.0
    cav = first_num(r['cavities'], 0.0)
    cyc = first_num(r['cycle_time_s'], 0.0)
    mc_txt = r['mold_cost_usd']
    mold = 0.0 if mc_txt.strip().upper().startswith('UNKNOWN') or mc_txt.strip().lower().startswith('n/a') else mid_range(mc_txt)
    clamp = first_num(r['clamp_required_t'], 0.0) if not r['clamp_required_t'].strip().lower().startswith('n/a') else 0.0
    shot = first_num(r['shot_weight_g'], 0.0) if not r['shot_weight_g'].strip().lower().startswith('n/a') else 0.0
    m_eq = re.search(r'PP-eq\s*([\d.]+)', r['clamp_required_t'])
    shot_eq = float(m_eq.group(1)) if m_eq else (shot * 0.9 / density(mat) if shot else 0.0)
    width = first_num(r['mold_size_mm'], 0.0) if nums(r['mold_size_mm']) else 0.0
    non_inj = fit in ('Other process', 'Requires extrusion', 'Requires blow molding')
    if non_inj or not clamp:
        press, pnote, cav_eff = 999, '', cav
    else:
        press, pnote, cav_eff = min_press(clamp, shot_eq, width, cav)
    unit_cost = first_num(r['unit_cost_dzd']) if nums(r['unit_cost_dzd']) else None

    # price cascade
    basis_note = ''
    if pid in RETAIL:
        rp, lab = RETAIL[pid]
        price, basis = round(rp * 0.55, 2), lab
    elif pid in FOB:
        price, basis = round(FOB[pid] * FX, 2), 'ASSUMPTION'
    else:
        pot = r['potential_price_dzd']
        pv = first_num(pot) if (nums(pot) and not pot.strip().upper().startswith('UNKNOWN')) else None
        if pv is not None and pv > 0:
            price, basis = round(pv, 2), 'ASSUMPTION'
        elif pid in LONGLIST:
            price, basis = round(LONGLIST[pid][0] * 0.55, 2), 'ASSUMPTION'
            basis_note = 'longlist'
        else:
            price, basis = 0.0, 'UNKNOWN'
    vol = VOL[pid]
    vbasis = 'WEAK SIGNAL' if pid in VOL_WEAK else 'ASSUMPTION'

    # evidence
    if pid in EV2: ev = 2
    elif pid in EV0: ev = 0
    else: ev = 1

    # verdict / kill reason
    verdict, kreason = verdict_and_reason(pid, r)
    for mr in mrows:
        mv, _ = verdict_and_reason(mr['product_id'], mr)
        if mv and mv not in verdict:
            verdict = f'{verdict} / {mr["product_id"]}: {mv}'

    # hard kill
    hk = ''
    if non_inj and pid != 'OS-098':
        if pid in ('CL-023', 'CL-024', 'CL-025', 'CL-026'):
            hk = 'Multi-part pump/trigger assembly (springs, balls, automatic assembly)'
        else:
            hk = 'Not injection: ' + {'Requires extrusion': 'extrusion', 'Requires blow molding': 'blow molding'}.get(fit, 'other process (rubber/steel/CNC)')
    elif press == 999 and pid != 'OS-098':
        hk = 'Needs >160 t press (beyond founder press)'
    if not hk and pid in CERT_KILL:
        hk = CERT_KILL[pid]
    if not hk:
        mres = HARD_RESIN.search(mat or '')
        if mres:
            hk = f'{mres.group(1)}: no local stockist in small lots (Phase 1 resin trigger; lift only if a stockist is confirmed)'
    elif pid in CERT_KILL and CERT_KILL[pid] not in hk:
        hk = hk + '; ' + CERT_KILL[pid]

    # scores
    dem, sho, imp, loc, rec, pay, spd, sku, cus = PROF[pid]
    if pid == 'OS-043': dem = 2
    s_cust = sc_cust(r['buyer_concentration'])
    if pid in ('OS-069', 'OS-112', 'OS-068'): s_cust = 1
    if pid in ('OS-025', 'OS-026', 'OS-063'): s_cust = 3
    if pid in ('OS-024',): s_cust = 1
    if pid in ('OS-073', 'OS-098', 'OS-067'): s_cust = 4
    if pid in ('OS-039', 'OS-046', 'OS-047', 'OS-030', 'OS-031', 'OS-033', 'OS-034', 'OS-035', 'OS-036', 'OS-037', 'OS-038', 'OS-044', 'OS-045'):
        s_cust = 4  # few appliance OEMs
    if pid.startswith('OS-10') and pid in ('OS-107', 'OS-108', 'OS-109', 'OS-110'): s_cust = 3
    if pid == 'OS-083': s_cust = 3

    margin = None
    if price > 0 and unit_cost is not None and basis != 'UNKNOWN':
        margin = (price - unit_cost) / price
    s_mar = sc_margin(margin)
    if basis_note == 'longlist': s_mar = min(s_mar, 7)
    if pid == 'CL-004': s_mar = 5  # quote-based, customer-funded mold

    s_sw = sc_switch(r['switching_difficulty'])
    s_mold = sc_mold(mold)
    if pid == 'CL-004': s_mold = 8      # brand-funded mold
    if pid == 'CL-003': s_mold = 7      # reuses CL-002 mold (US$14k) - no extra tool
    if pid in ('CL-023', 'CL-024', 'CL-025', 'CL-026'): s_mold = 0
    if pid == 'OS-098': s_mold = 7      # customer-funded tooling
    if pid in ('OS-011',): s_mold = 1   # 12-18 tools per size family

    if non_inj:
        s_mc = 5 if pid == 'OS-098' else 0
    elif fit.startswith('Fits'):
        s_mc = 10 if press <= 120 else 8
    elif fit.startswith('Borderline'):
        s_mc = 6
    else:  # requires larger
        s_mc = 4 if press <= 120 else (2 if press == 160 else 1)

    s_res = sc_resin(mat)
    s_tech, s_qr = sc_quality(r['quality_difficulty'])
    if pid in ('CL-001', 'CL-002', 'CL-003', 'CL-004', 'CL-021', 'CL-022'): s_tech = 4  # IMC hinge tooling
    if pid in ('CL-005', 'CL-006', 'CL-009', 'CL-018', 'CL-020', 'IF-09', 'IF-10'): s_tech = min(s_tech, 5)  # 2-3 molds + assembly
    if pid in ('CL-014', 'JC-37', 'OS-011'): s_tech = min(s_tech, 4)  # unscrewing cores
    if pid in ('IF-43', 'IF-44', 'IF-45', 'OS-055', 'OS-058', 'OS-096', 'OS-009'): s_tech = min(s_tech, 5)  # insert loading
    if pid in ('IF-21', 'IF-22', 'IF-28'): s_qr = 3   # pressure / leak-free seat
    if pid in ('JC-18', 'IF-53'): s_qr = 2            # structural / castor load
    if pid in ('OS-009', 'OS-010', 'JC-37'): s_qr = 5   # pull-out performance
    if pid in ('OS-068', 'OS-069', 'OS-112'): s_qr = 3
    if pid == 'OS-043': s_qr = 2
    s_reg = sc_reg(r['regulatory_difficulty'])
    if pid in ('CL-028', 'CL-029'): s_reg = 7
    s_copy = sc_copy(r['copy_risk'])
    if pid in ('CL-023', 'CL-024', 'CL-025', 'CL-026'): s_copy = 6
    if pid == 'CL-027': s_copy = 3
    s_wc = sc_wc(r['working_capital'], sector, mat)
    if pid == 'OS-068' or pid == 'OS-112': s_wc = 2

    # utilization (only if it runs on the founder's 100-120 t press)
    if non_inj or press > 120 or not cav_eff or not cyc:
        s_util = 0
        hours = 0
    else:
        hours = vol / cav_eff * cyc / 3600 / 0.8
        s_util = sc_util(hours)

    # pain summary
    pe = r['pain_evidence']
    ps = f"{r['pain_type']} ({r['pain_confidence'] or 'UNKNOWN'}): {short(pe, 200)}"
    for mr in mrows:
        if mr['pain_type'] != 'none_found':
            ps += f" | {mr['product_id']}: {mr['pain_type']} - {short(mr['pain_evidence'], 100)}"

    kb = r['known_buyers']
    for mr in mrows:
        kb += f" | {mr['product_id']} buyers: {mr['known_buyers']}"
    kb = short(kb, 400)

    product = r['product']
    if merged:
        product = f"{product} [merged duplicates: {pid} + {' + '.join(merged)}]"

    # next action
    nxt = (r['next_validation_action'] or '').strip()
    m = re.match(r'^(?:As|Same as)\s+((?:CL|JC|IF|OS)-\d+)(.*)$', nxt)
    if m and m.group(1) in rows:
        nxt = rows[m.group(1)]['next_validation_action'].strip() + m.group(2)
    if pid in NEXT_OVR:
        nxt = NEXT_OVR[pid]
    killed_by_researcher = bool(re.search(r'KILL|FUTURE', verdict, re.I)) and 'INVESTIGATE' not in verdict.upper()
    if (not nxt or GENERIC_NEXT_BAD.match(nxt)) and pid not in NEXT_OVR:
        if killed_by_researcher or hk:
            nxt = 'No action: killed; re-open only if a named buyer asks for this part'
        else:
            nxt = 'Price + origin check of this part with 3 distributors (DZD per 1,000, MOQ, stock-outs)'
    elif killed_by_researcher and not nxt.lower().startswith('no action') and pid not in NEXT_OVR and pid not in ('CL-028',):
        nxt = 'No action: killed; re-open only if a named buyer asks for this part'
    if hk.startswith(('POM', 'ABS', 'PC', 'PBT', 'ASA', 'TPE', 'TPU')) and not killed_by_researcher:
        res = hk.split(':')[0]
        nxt = f'Gate: confirm a local {res} stockist selling 25 kg lots (Polychimical/Distripol); if none, drop. Then: ' + nxt
    if pnote:
        nxt = nxt.rstrip('. ') + f'. [Press note: {pnote}]'
    if basis == 'UNKNOWN' and not hk:
        nxt = nxt.rstrip('. ') + '. [No price found anywhere: get a DZD price first]'

    rec_out = {
        'product_id': pid, 'product': product, 'family': r['family'], 'sector': sector, 'machine_fit': fit,
        'material': mat, 'part_weight_g': round(pw_v, 2), 'cavities': int(cav), 'cycle_s': round(cyc, 1),
        'mold_cost_usd': int(round(mold)), 'price_dzd': price, 'price_basis': basis,
        'annual_volume_pcs': vol, 'volume_basis': vbasis, 'clamp_t': round(clamp, 1), 'shot_g': round(shot, 1),
        'min_press_t': press, 'evidence_strength': ev, 'pain_summary': short(ps, 330), 'known_buyers': kb,
        's_demand': dem, 's_shortage': sho, 's_import_dep': imp, 's_local_comp': loc, 's_cust_conc': s_cust,
        's_recurring': rec, 's_margin': s_mar, 's_switching': s_sw, 's_custom_b2b': cus, 's_mold_afford': s_mold,
        's_machine_compat': s_mc, 's_resin_avail': s_res, 's_tech': s_tech, 's_regulatory': s_reg,
        's_quality_risk': s_qr, 's_copy_risk': s_copy, 's_payment_risk': pay, 's_wc': s_wc, 's_speed': spd,
        's_sku_family': sku, 's_utilization': s_util, 'hard_kill': hk, 'kill_reason': short(kreason, 250),
        'researcher_verdict': verdict, 'next_validation_action': short(nxt, 330)}
    out.append(rec_out)

with open(OUT, 'w', newline='', encoding='utf-8') as fh:
    w = csv.DictWriter(fh, fieldnames=COLS, quoting=csv.QUOTE_MINIMAL)
    w.writeheader()
    for o in out:
        w.writerow(o)
print('wrote', len(out), 'rows to', OUT)
