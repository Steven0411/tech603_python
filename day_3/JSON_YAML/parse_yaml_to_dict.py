import yaml

with open("servers.yaml", "r") as file:
    servers = yaml.safe_load(file)

print(type(servers))

print(servers.get("server1"))

for record, key in servers.get("server1").items():
    print(f'{key}: {record}')

print(servers.get("server2"))

for record, key in servers.get("server2").items():
    print(f'{key}: {record}')