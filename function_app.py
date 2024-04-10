import azure.functions as func
import logging
import json

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.route(route="http_trigger")
def http_trigger(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    req_body = req.get_json()
    readings = req_body.get('readings')
    for r in readings:
        if r['temperature'] <= 25:
            r['status'] = 'ok'
        elif r['temperature'] < 50:
            r['status'] = 'caution'
        elif r['temperature'] < 50:
            r['status'] = 'warning'
    response_dict = {"readings": readings}
    response_body = json.dumps(response_dict, indent=2)
    return func.HttpResponse(body=response_body, mimetype="application/json")