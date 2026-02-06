# policy-driven-llm-routing

Routes chat, builder, and researcher modes via JSON policy with provider fallbacks, jury consensus, and swarm patterns.

## Purpose
Centralize model/provider selection and orchestration behavior into policy files so runtime behavior is controlled by config, not code edits.

## Features
- Mode-aware routing (`chat`, `builder`, `researcher`) via `routing_policy.json`.
- Ordered fallback chains per mode/provider.
- Jury execution strategy for multi-model consensus.
- Swarm patterns for parallel and tree-structured execution.
- Deterministic policy validation before runtime start.

## Config
- `routing_policy.json`: Primary routing, fallback, jury, and swarm definitions.
- `ROUTING_POLICY_PATH`: Override path for policy file.
- `DEFAULT_MODE`: Runtime default mode if one is not specified.
- `MAX_PARALLEL_AGENTS`: Ceiling for swarm fan-out.
- `JURY_MIN_AGREEMENT`: Minimum agreement threshold for jury outcomes.

## Quickstart
```bash
cp routing_policy.example.json routing_policy.json
python3 validate_routing_policy.py routing_policy.json
python3 router.py --mode researcher --input "Summarize latest status"
```

## Roadmap
- Add schema versioning and migration tooling for policy files.
- Add weighted provider scoring based on task type.
- Add cost-aware routing constraints and budget caps.
- Add visual policy inspector for fallback/jury/swap paths.
