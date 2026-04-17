import json

# Convert a Python dictionary into a JSON-formatted string and a JSON file

servers_dict = {
    "server1": {
        "hostname": "web-server-1",
        "ip_address": "192.168.1.1",
        "role": "web",
        "status": "active"
    },
    "server2": {
        "hostname": "db-server-1",
        "ip_address": "192.168.1.2",
        "role": "database",
        "status": "maintenance"
    }
}
# dumps -returns string
json_string = json.dumps(servers_dict, indent=4)
print(json_string)

with open("servers.json", "w") as outfile:
    # dump - returns stream that can be written to a file
    json.dump(servers_dict, outfile, indent=4)
    # could also use:
    # f.write(json.dumps(server_dict, indent=4))