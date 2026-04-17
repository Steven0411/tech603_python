import json

with open("servers.json", "r") as infile:
    #json.loads errors because json.loads expects a string not a file
    # servers = json.loads(file)

    # converts the file to a json string to be read by json.loads
    json_str = infile.read()

    # json.loads reads the json string and formats it into the dict
    servers = json.loads(json_str)

print(type(servers))

for key, value in servers.items():
    print(f'Key and Value: {key}: {value}')
    for subkey, subvalue in value.items():
        print(f'Record key and sub value: {subkey}: {subvalue}')