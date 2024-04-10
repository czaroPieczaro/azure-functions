import azure.functions as func
import logging

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.route(route="http_trigger")
def http_trigger(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    req_body = req.get_json()
    readings = req_body.get('readings')
    print(readings)
    name = req_body.get('name')
    print(name)
    # if not name:
    #     try:
    #         req_body = req.get_json()
    #     except ValueError:
    #         pass
    #     else:
    #         name = req_body.get('name')
    # for r in readings:
    #     print(r)

    return func.HttpResponse(f"Hello, {readings}. This HTTP triggered function executed successfully.")