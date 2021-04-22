from flask import Flask, request, jsonify, render_template
from samp_client.client import SampClient
import sys
app = Flask(__name__)

# def Samp():
#     with SampClient(address='203.248.21.223', port=7777) as client:
#         info = client.get_server_clients_detailed()
#         return str(info)




@app.route('/keyboard')
def Keyboard():
    return "hello"

@app.route('/message', methods=['POST'])
def Message():
    result = []
    with SampClient(address='203.248.21.223', port=7777) as client:
        info = client.get_server_clients_detailed()
        players = client.get_server_info()
        for i in info:
            result.append(i[1])
    
    content = request.get_json()
    content = content['userRequest']
    content = content['utterance']
    
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
                            "text" : f"현재 서버 인원은 {players.players}명입니다!\n" + f"{str(result)}"
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
