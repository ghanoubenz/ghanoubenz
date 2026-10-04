"""Run the study's MiroFish simulation via the local MiroFish backend API.
Prereqs: MiroFish running (`npm run dev` in MiroFish root) with LLM_API_KEY, LLM_BASE_URL,
LLM_MODEL_NAME and ZEP_API_KEY set in MiroFish/.env, and network access to the LLM and Zep Cloud.
Usage: python run_mirofish.py [requirement_number 1-5] [max_rounds]
Every result is a SIMULATED OUTCOME, not evidence."""
import sys, time, re, pathlib, requests

API = "http://localhost:5001/api"
HERE = pathlib.Path(__file__).parent
SEEDS = [HERE / "seed-uae-line-continuity.md"]

def requirement(n: int) -> str:
    text = (HERE / "simulation-requirements.md").read_text()
    items = re.findall(r"^\d+\.\s+\*\*.*?\*\*\s+(.*)$", text, re.M)
    return items[n - 1]

def wait(url, payload=None, key="status", done=("completed",), every=10):
    while True:
        r = (requests.post(url, json=payload) if payload is not None else requests.get(url)).json()
        st = (r.get("data") or {}).get(key)
        print("  ...", st, (r.get("data") or {}).get("progress", ""))
        if st in done: return r["data"]
        if st == "failed": raise SystemExit(r)
        time.sleep(every)

def main():
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    rounds = int(sys.argv[2]) if len(sys.argv) > 2 else 30
    req = requirement(n)
    files = [("files", (p.name, p.read_bytes(), "text/markdown")) for p in SEEDS]
    r = requests.post(f"{API}/graph/ontology/generate", files=files,
                      data={"simulation_requirement": req, "project_name": f"uae-line-continuity-q{n}"}).json()
    pid = r["data"]["project_id"]; print("project", pid)
    t = requests.post(f"{API}/graph/build", json={"project_id": pid}).json()["data"]["task_id"]
    wait(f"{API}/graph/task/{t}")
    sim = requests.post(f"{API}/simulation/create", json={"project_id": pid}).json()["data"]["simulation_id"]
    requests.post(f"{API}/simulation/prepare", json={"simulation_id": sim})
    wait(f"{API}/simulation/prepare/status", {"simulation_id": sim}, done=("completed", "ready"))
    requests.post(f"{API}/simulation/start", json={"simulation_id": sim, "platform": "parallel", "max_rounds": rounds})
    print("simulation started:", sim, "- monitor in the MiroFish UI (http://localhost:3000); then:")
    input("Press Enter once the run has finished to generate the report...")
    requests.post(f"{API}/report/generate", json={"simulation_id": sim})
    wait(f"{API}/report/generate/status", {"simulation_id": sim})
    print(f"Report ready: GET {API}/report/by-simulation/{sim}  (label: SIMULATED OUTCOME)")

if __name__ == "__main__":
    main()
