# Phase 0 — Tool Setup Report

UAE Engineering + Industrial + AI-Enabled Business Opportunity Discovery.
Date: 2026-10-04. Environment: ephemeral cloud container (Linux, Python 3.11, Node 22, uv 0.8).

## Summary

| Tool | Install | Runs | Usable for research right now |
|---|---|---|---|
| Agent Reach v1.5.0 (`Panniantong/Agent-Reach` @ `a19a171`, 2026-09-16) | ✅ | ✅ `agent-reach doctor` works | ❌ Mostly no. The container's network policy blocks nearly every target host |
| MiroFish v0.1.0 (`666ghj/MiroFish` @ `7657031`, 2026-10-02) | ✅ | ✅ Backend boots, API answers, frontend builds | ❌ No. It needs an LLM API key plus a Zep Cloud key, and both endpoints are blocked |

## Agent Reach

Installed per `docs/install.md` into an isolated venv (`~/.agent-reach-venv`), outside this repo.
Ran the read-only check (`install --env=auto`), the dry run, then `install --env=auto --system` for the
core zero-login channels only (mcporter + Exa MCP config, yt-dlp Node runtime). No login-based channel was installed.

### `agent-reach doctor`: 3/16 channels marked available

Doctor's "available" status does not mean the channel works from this container.
I tested every channel live:

| Channel | Doctor | Live test from this container | Notes |
|---|---|---|---|
| Web (Jina Reader `r.jina.ai`) | ✅ | ❌ proxy 403 | Network policy |
| YouTube (yt-dlp) | ✅ | ❌ proxy 403 | Network policy |
| RSS (feedparser) | ✅ | ❌ for any blocked feed host | Network policy |
| Exa semantic search (mcporter) | ⚠️ | ❌ | `mcp.exa.ai` blocked, **and** Exa MCP now asks for OAuth browser approval (timed out headless) |
| GitHub (gh CLI) | ⚠️ | partial | `api.github.com` reachable; doctor won't live-verify auth |
| V2EX / Xueqiu | ⚠️ | ❌ proxy 403 | Not relevant to this project |
| Reddit | ❌ off | ❌ | **Login is mandatory** (anonymous API blocked upstream). Needs OpenCLI + your Chrome session (desktop), or `rdt-cli` + a cookie you export |
| Twitter/X | ⚠️ | ❌ | Needs `twitter-cli` + Cookie-Editor export from **your** account |
| LinkedIn | ⚠️ | ❌ | Public pages via Jina (blocked here). Full access needs `mcp-server-linkedin` + **your** manual browser login |
| Facebook / Instagram | ❌ off | ❌ | OpenCLI + **your** logged-in desktop Chrome only. Not supported on servers |
| Bilibili / Xiaohongshu / Boss / Xiaoyuzhou | ❌ off | — | Not relevant to this project |

### Reachability probe (through container egress proxy)

Blocked (403 CONNECT): r.jina.ai, google.com, youtube.com, reddit.com, old.reddit.com, mcp.exa.ai, api.exa.ai, x.com,
linkedin.com, facebook.com, instagram.com, bing.com, duckduckgo.com, wikipedia.org, moiat.gov.ae, u.ae,
thenationalnews.com, gulfnews.com, zawya.com, khaleejtimes.com, huggingface.co, api.openai.com,
dashscope.aliyuncs.com, api.zep.ai, api.getzep.com.

Reachable: api.github.com, api.anthropic.com, package registries (PyPI, npm).

The assistant's built-in web search works but returns only titles and snippets. It doesn't surface Reddit threads
reliably and can't open Reddit pages. Built-in page fetch is subject to the same egress block.

## MiroFish

Installed per README (`npm run setup` + `cd backend && uv sync`). The backend venv is ~7 GB: camel-oasis pulls torch,
transformers and triton. Smoke test using placeholder keys: the Flask app starts, and `/api/graph/project/list` and
`/api/simulation/list` return 200. OASIS 0.2.5 and camel-ai 0.2.78 import cleanly. `vite build` succeeds.

Runtime requirements (checked in `backend/app/config.py`; startup refuses without them):

- `LLM_API_KEY` / `LLM_BASE_URL` / `LLM_MODEL_NAME`: any OpenAI-compatible endpoint. Default is Alibaba DashScope `qwen-plus`.
  `api.anthropic.com` is reachable from this container and offers an OpenAI-compatible endpoint, so an Anthropic API
  key would work with the current network policy (untested: needs your key).
- `ZEP_API_KEY`: **Zep Cloud only.** Self-hosted Zep is explicitly rejected (`ZEP_API_URL` unsupported). Zep hosts are
  blocked, so the network policy must allow them.
- Cost warning from upstream: token consumption is high. Start with fewer than 40 simulation rounds.

How it works: you upload seed documents (PDF/MD/TXT), it builds a GraphRAG knowledge graph in Zep, generates agent
personas, then runs Twitter-like or Reddit-like social simulations (OASIS) followed by a ReportAgent.
Its output is a **social-opinion simulation**. Every result must be labelled **SIMULATED OUTCOME**.

## What is needed from the user before Phase 1

1. **Network access (required).** In the cloud environment settings (environment menu → Edit → Network access),
   choose a broader level or Custom, keep the default package-manager list, and add at least:
   `reddit.com, www.reddit.com, old.reddit.com, r.jina.ai, mcp.exa.ai, youtube.com, www.youtube.com, google.com`,
   plus UAE sources (`u.ae, moiat.gov.ae, khaleejtimes.com, gulfnews.com, thenationalnews.com, zawya.com`).
   Unrestricted access is simplest for open-ended research.
   Docs: https://code.claude.com/docs/en/cloud-environments#network-access
2. **Reddit (strongly recommended, since it's the main source).** Agent Reach has no anonymous Reddit path. Options:
   (a) export a cookie from a dedicated Reddit account with Cookie-Editor and provide it for `rdt-cli`; or
   (b) run the research from a desktop session with OpenCLI using your own Chrome login.
   Upstream recommends a secondary account because of ban risk.
3. **Exa search.** The Exa MCP endpoint now requests OAuth browser approval, which you would need to complete
   (or provide an Exa API key).
4. **Optional:** Twitter/X cookie (Cookie-Editor export, secondary account), LinkedIn login (manual browser login).
   Facebook/Instagram only work from a desktop with your logged-in Chrome.
5. **MiroFish (only needed at Phase 5).** An LLM API key (OpenAI-compatible; Anthropic works with current policy) and
   a Zep Cloud API key (free tier), plus network access to Zep.

No authentication was bypassed and no credentials were obtained.

## Reproduce in a fresh container

```bash
python3 -m venv ~/.agent-reach-venv
~/.agent-reach-venv/bin/pip install https://github.com/Panniantong/agent-reach/archive/main.zip
export PATH=~/.agent-reach-venv/bin:$PATH
agent-reach install --env=auto --system      # core zero-login channels only
agent-reach doctor

git clone --depth 1 https://github.com/666ghj/MiroFish.git ~/tools/MiroFish
cd ~/tools/MiroFish && cp .env.example .env   # then fill LLM_* and ZEP_API_KEY
npm run setup && (cd backend && uv sync)
npm run dev                                   # frontend :3000, backend :5001
```
