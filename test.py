from flask import Flask, request, jsonify
from samp_client.client import SampClient
import sys
app = Flask(__name__)

with SampClient(address='203.248.21.223', port=7777) as client:
    info = client.get_server_info()

@app.route('/keyboard')
def Keyboard():
    return "test"

@app.route('/message', methods=['POST'])
def Message():
    
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
                            "text" : f"현재 서버인원은 {info.players}명\n" + f"{info.gamemode}\n라운드가 진행중입니다!"
                        }
                    }
                ]
            }
        }
    return jsonify(dataSend)

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')