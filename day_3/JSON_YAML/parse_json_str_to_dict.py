import json

with open("servers.json", "r") as file:
    #json.loads errors because json.loads expects a string not a file

    # converts the file to a json string to be read by json.loads
    json_str = file.read()
    # json.loads reads the json string and formats it into the dict
    servers = json.loads(json_str)

print(type(servers))

print(servers.get("server1"))

for record, key in servers.get("server1").items():
    print(f'{key}: {record}')

print(servers.get("server2"))

for record, key in servers.get("server2").items():
    print(f'{key}: {record}')