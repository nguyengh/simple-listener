import logging.config

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import json

# Load logging configuration
with open('logging.json', 'r') as config_file:
    config_dict = json.load(config_file)
    logging.config.dictConfig(config_dict)

app = FastAPI()

LOG = logging.getLogger()

@app.get("/")
async def root():
    return JSONResponse(content="Hello World!", status_code=200)

@app.post("/redfish-event")
async def receive_redfish_event(request: Request):
    event_data = await request.json()
    LOG.info("Received Redfish Event: %s", event_data)
    return JSONResponse(content={"message": "Event received successfully"}, status_code=200)
