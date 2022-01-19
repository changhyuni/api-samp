from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from samp_client.client import SampClient
from pydantic import BaseModel
from typing import Optional, List
import json


with SampClient(address='14.35.79.33', port=7777) as client:
    ServerInfo = client.get_server_info()

app = FastAPI()


class SendInBase(BaseModel):
    utterance: str

class SendIn(BaseModel):
    userRequest: List[SendInBase]

@app.get('/heartbeat')
async def health_check():                   
    return "OK"

@app.post("/send/", description="데이터 보내는 API")
async def send_data(send: SendIn):
    send = send.userRequest[0].utterance
    if send == '인원':
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
    else:
        content = "x"
        
    return content


