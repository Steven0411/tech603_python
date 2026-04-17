import yaml
import os
import sys

if len(sys.argv) > 1:

    if os.path.exists(sys.argv[1]):

        file = open(sys.argv[1], "r")

        yaml.safe_load(file)
        file.close()
        print("YAML file is valid!")
    else:

        print("ERROR: File '" + sys.argv[1] + "' not found")
else:
    print("ERROR: No YAML file was specified to check")
    print(f"Usage: {sys.argv[0]} <YAML filename>")