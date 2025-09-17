import json
import logging
import azure.functions as func

# Minimal stub: validate shape and return 202 Accepted.
def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        body = req.get_json()
    except ValueError:
        return func.HttpResponse(
            json.dumps({"error": "Invalid JSON"}),
            status_code=400,
            mimetype="application/json"
        )

    required = ["requestId", "action"]
    missing = [k for k in required if k not in body]
    if missing:
        return func.HttpResponse(
            json.dumps({"error": f"Missing fields: {','.join(missing)}"}),
            status_code=400,
            mimetype="application/json"
        )

    logging.info("Ingest received request %s", body.get("requestId"))
    return func.HttpResponse(
        json.dumps({"status": "accepted", "requestId": body["requestId"]}),
        status_code=202,
        mimetype="application/json"
    )