import yaml

with open("servers.yaml", "r") as file:
    servers = yaml.safe_load(file)

print(type(servers))

for key, value in servers.items():
    print(f'Key and Value: {key}: {value}')
    for subkey, subvalue in value.items():
        print(f'Record key and sub value: {subkey}: {subvalue}')