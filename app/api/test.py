from samp_client.client import SampClient

with SampClient(address='14.35.79.33', port=7777) as client:
    ServerInfo = client.get_server_info()

print(type(ServerInfo.players))