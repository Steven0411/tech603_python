import json

with open("servers.json", "r") as infile:
    servers = json.load(infile)

print(type(servers))

for key, value in servers.items():
    print(f'Key and Value: {key}: {value}')
    for subkey, subvalue in value.items():
        print(f'Record key and sub value: {subkey}: {subvalue}')