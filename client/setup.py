import argparse
import json
import os

parser = argparse.ArgumentParser(description="Process command line arguments.")

parser.add_argument('--key', type=str, required=True, help="The Secret Key")
parser.add_argument('--ip', type=str, required=True, help="The IP address of the Server")
parser.add_argument('--remove', type=str, required=True, help="Should the setup file be removed?")

args = parser.parse_args()

ip_address = args.ip
key = args.key

with open('setting.json', 'w') as f:
    data = {
        "ip": ip_address,
        "key": key
    }
    json.dump(data, f, indent=4)

f.close()

if args.remove == "True":
    os.remove(__file__)