import azure.functions as func
import logging

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.route(route="http_trigger")
def http_trigger(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    readings = req.params.get('readings')
    print(readings)
    for r in readings:
        print(r)

    return func.HttpResponse(f"Hello, {readings}. This HTTP triggered function executed successfully.")