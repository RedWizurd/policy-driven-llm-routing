import argparse
import json
from pathlib import Path


def load_policy(path: str) -> dict:
    return json.loads(Path(path).read_text())


def route(mode: str, user_input: str, policy: dict) -> dict:
    mode_cfg = policy["modes"][mode]
    primary = mode_cfg["providers"][0]
    fallbacks = mode_cfg["providers"][1:]
    return {
        "mode": mode,
        "input_preview": user_input[:80],
        "primary_provider": primary,
        "fallbacks": fallbacks,
        "jury": mode_cfg["jury"],
        "swarm": mode_cfg["swarm"],
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Policy-driven routing preview")
    parser.add_argument("--mode", required=True, choices=["chat", "builder", "researcher"])
    parser.add_argument("--input", required=True)
    parser.add_argument("--policy", default="routing_policy.json")
    args = parser.parse_args()

    policy = load_policy(args.policy)
    print(json.dumps(route(args.mode, args.input, policy), indent=2))


if __name__ == "__main__":
    main()
