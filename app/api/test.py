from samp_client.client import SampClient


with SampClient(address='14.35.79.33', port=6969, rcon_password='nclubkorea123') as client:
    info = client.get_server_info()
    print(info)


with SampClient(address='14.35.79.33', port=32085) as client:
        TwoServerInfo = client.get_server_info()
        print(TwoServerInfo)

