from samp_client.client import SampClient
from flask import Flask

app = Flask(__name__)

def Samp():
    with SampClient(address='203.248.21.223', port=7777) as client:
        info = client.get_server_info()
        result = f"서버인원 {info.players}명", info.gamemode, info.hostname
    return str(result)

@app.route("/api")
def hello():
    return Samp()

if __name__ == '__main__':
    app.run(debug=True)

