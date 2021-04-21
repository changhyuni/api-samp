from flask import Flask, request, jsonify
from samp_client.client import SampClient
import sys
app = Flask(__name__)

def Samp():
    with SampClient(address='203.248.21.223', port=7777) as client:
        info = client.get_server_info()
        result = f"서버인원 {info.players}명", info.gamemode, info.hostname
    return result


@app.route('/keyboard')
def Keyboard():
    dataSend = {
    }
    return jsonify(dataSend)

@app.route('/message', methods=['POST'])
def Message():
    
    content = request.get_json()
    content = content['userRequest']
    content = content['utterance']
            response_data = {
                "version": "2.0",
                "template": {
                    "outputs": [
                        {"simpleText": 
                        "text": returnMenu(ChoiceUrl, ChoiceDay)}
                        }
                        ],
                    "quickReplies": [{"label": "처음으로", "action": "message", "messageText": "처음으로"},
                                     ]
                }
            }
    
    if content == u"안녕":
        dataSend = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "carousel": {
                            "type" : "basicCard",
                            "items": [
                                {
                                    "title" : "",
                                    "description" : "인원"
                                }
                            ]
                        }
                    }
                ]
            }
        }
    else :
        dataSend = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "simpleText":{
                            "text" : f"{Samp()}"
                        }
                    }
                ],
                "quickReplies": [
                    {"label": "인원", "action": "message", "messageText": "인원"},
                ]
            }
        }
    return jsonify(dataSend)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
