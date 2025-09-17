import json
import logging

# Minimal stub: just log whatever arrives from the queue.
def main(msg: str) -> None:
    try:
        payload = json.loads(msg)
    except Exception:
        payload = {"raw": msg}
    logging.info("ProvisionJob picked up message: %s", payload)