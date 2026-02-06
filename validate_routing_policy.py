import json
import sys
from pathlib import Path

REQUIRED_MODE_KEYS = {"providers", "jury", "swarm"}


def validate(path: Path) -> int:
    data = json.loads(path.read_text())
    if "modes" not in data or not isinstance(data["modes"], dict):
        print("Invalid policy: missing object key 'modes'")
        return 1

    for mode in ("chat", "builder", "researcher"):
        if mode not in data["modes"]:
            print(f"Invalid policy: missing mode '{mode}'")
            return 1
        mode_cfg = data["modes"][mode]
        missing = REQUIRED_MODE_KEYS - set(mode_cfg.keys())
        if missing:
            print(f"Invalid policy: mode '{mode}' missing keys: {sorted(missing)}")
            return 1
        if not isinstance(mode_cfg["providers"], list) or not mode_cfg["providers"]:
            print(f"Invalid policy: mode '{mode}' providers must be a non-empty list")
            return 1

    print("Routing policy valid")
    return 0


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: python3 validate_routing_policy.py <routing_policy.json>")
        raise SystemExit(2)
    raise SystemExit(validate(Path(sys.argv[1])))


if __name__ == "__main__":
    main()
