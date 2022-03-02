from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from samp_client.client import SampClient
from pydantic import BaseModel
from typing import Optional, List, Any, Dict, AnyStr, Union
import json

app = FastAPI()

JSONObject = Dict[AnyStr, Any]
JSONArray = List[Any]
JSONStructure = Union[JSONArray, JSONObject]

round_info = ''

@app.get('/heartbeat')
async def health_check():                   
    return "OK"

@app.post("/")
async def root(arbitrary_json: JSONStructure = None):

    UserList = ''
    TwoUserList = ''
    with SampClient(address='14.35.79.33', port=6969) as client:
        ServerInfo = client.get_server_info()
        UserInfo = client.get_server_clients()

    for User in UserInfo:
        UserList += User.name + '\n'

    with SampClient(address='14.35.79.33', port=32085) as client:
        TwoServerInfo = client.get_server_info()
        TwoUserInfo = client.get_server_clients()


    for TwoUser in TwoUserInfo:
        TwoUserList += TwoUser.name + '\n'

    

    
    round_info = ''
    players = ServerInfo.players
    Twoplayers = TwoServerInfo.players

    Tworound_info = '대기' if TwoServerInfo.gamemode == 'Att-Def v1.23 (r)' else '게임'
    round_info = '대기' if TwoServerInfo.gamemode == 'Att-Def v1.23 (r)' else '게임'

    content = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText":{
                        "text" : "1서버에 "f'{players}'"명이 " f'{round_info} ' "중입니다! \n\n<유저리스트>\n"f'{UserList}'" \n2서버에 "f'{Twoplayers}'"명이 " f'{Tworound_info} ' "중입니다! \n\n<유저리스트>\n"f'{TwoUserList}'""

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



