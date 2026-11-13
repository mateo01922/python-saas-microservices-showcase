"""Public example client demonstrating calls to the unified RapidAPI / Render gateway."""

import os
import requests

GATEWAY_URL = os.environ.get("GATEWAY_BASE_URL", "http://127.0.0.1:8000").rstrip("/")


def main() -> None:
    health = requests.get(f"{GATEWAY_URL}/health", timeout=10)
    print("Gateway health:", health.status_code, health.json())

    guardrail = requests.post(
        f"{GATEWAY_URL}/guardrail/v1/guardrail/inspect",
        json={"prompt": "System check: summarize Q4 invoice totals cleanly."},
        timeout=10,
    )
    print("Guardrail check:", guardrail.status_code, guardrail.json())


if __name__ == "__main__":
    main()
