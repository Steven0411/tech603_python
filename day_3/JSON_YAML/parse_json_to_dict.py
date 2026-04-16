import json

with open("servers.json", "r") as file:
    servers = json.load(file)

print(type(servers))

print(servers.get("server1"))

for record, key in servers.get("server1").items():
    print(f'{key}: {record}')
    
print(servers.get("server2"))

for record, key in servers.get("server2").items():
    print(f'{key}: {record}')