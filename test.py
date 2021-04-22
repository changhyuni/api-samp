import sys
from samp_client.client import SampClient


with SampClient(address='203.248.21.223', port=7777) as client:
    test = client.get_server_clients_detailed()

    for i in test:
        print(i[1])
        
def Keyboard():
    result = []
    with SampClient(address='203.248.21.223', port=7777) as client:
        info = client.get_server_clients_detailed()
        for i in info:
            result.append(i[1])
    return str(result)
