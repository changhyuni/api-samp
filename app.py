from samp_client.client import SampClient
from flask import Flask, request, jsonify

app = Flask(__name__)

def Samp():
    with SampClient(address='203.248.21.223', port=7777) as client:
        info = client.get_server_info()
        result = f"서버인원 {info.players}명", info.gamemode, info.hostname
    return str(result)

@app.route('/keyboard')
def Keyboard():
    dataSend = {
    }
    return jsonify(dataSend)

@app.route("/message", methods=['POST'])
def Message():
    
    content = request.get_json()
    content = content['userRequest']
    content = content['utterance']

    if content == u"인원":
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
                                    "description" : "안녕"
                                }
                            ]
                        }
                    }
                ]
            }
        }
    return jsonify(dataSend)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
