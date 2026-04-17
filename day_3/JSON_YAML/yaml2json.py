import json
import yaml
import os
import sys

if len(sys.argv) > 1:
    if os.path.isfile(sys.argv[1]):
        source_file = open(sys.argv[1], "r")
        source_content = yaml.safe_load(source_file)
        source_file.close()

    else:
        print(f"ERROR: {sys.argv[1]} does not exist")
        exit(1)

else:
    print("ERROR: No YAML file was specified")
    print("Usage: yaml2json.py <source_file.yaml> <target_file.json>")

json_data = json.dumps(source_content)

if len(sys.argv) > 2:
    print(f"printing to {sys.argv[2]}")
else:
    print("ERROR: No JSON file was specified")

if os.path.exists(sys.argv[2]):
    print(f"ERROR: {sys.argv[2]} already exists")
    exit(1)
else:
    print("file does not exist")

with open(sys.argv[2], "w") as file:
    file.write(json_data)