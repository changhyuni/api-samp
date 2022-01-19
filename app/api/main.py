from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from samp_client.client import SampClient
from pydantic import BaseModel
from typing import Optional, List, Any, Dict, AnyStr, Union
import json


with SampClient(address='14.35.79.33', port=7777) as client:
    ServerInfo = client.get_server_info()

app = FastAPI()

JSONObject = Dict[AnyStr, Any]
JSONArray = List[Any]
JSONStructure = Union[JSONArray, JSONObject]


@app.post("/")
async def root(arbitrary_json: JSONStructure = None):
    content = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText":{
                        "text" : f"{ServerInfo}"
                    }
                }
            ],
            "quickReplies": [
                {"label": "인원", "action": "message", "messageText": "인원"},
                {"label": "도움말", "action": "message", "messageText": "도움말"},
                {"label": "기능", "action": "message", "messageText": "기능"}
                ]
            }
        }
    return content

# with open('./skill.json', 'r') as f:
#     json_data = json.load(f)

@app.get('/heartbeat')
async def health_check():                   
    return "OK"

# @app.post("/send/", description="데이터 보내는 API")
# async def send_data(send: SendIn):
#     send = send.userRequest[0].utterance
#     if send == '인원':
#         content = {
#         "version": "2.0",
#         "template": {
#             "outputs": [
#                 {
#                     "simpleText":{
#                         "text" : f"{ServerInfo}"
#                     }
#                 }
#             ],
#             "quickReplies": [
#                 {"label": "인원", "action": "message", "messageText": "인원"},
#                 {"label": "도움말", "action": "message", "messageText": "도움말"},
#                 {"label": "기능", "action": "message", "messageText": "기능"}
#                 ]
#             }
#         }
#     else:
#         content = "x"
        
#     return content


