import json
import sys

def convert_env_to_json():
    try:
        dotenv = sys.argv[1]       
    except IndexError as e:
        dotenv = '.env'
    with open(dotenv, 'r') as f:
        content = f.readlines()
        data = dict([x.strip().split('=') for x in content if '=' in x and not x.startswith('#')])
    environment = []
    for key in data.keys():
        environment.append({"name":key,"value":data[key]})
    return list(environment)

def convert_secret_to_json():
    try:
        dotenv = sys.argv[1]       
    except IndexError as e:
        dotenv = '.env'
    with open(dotenv, 'r') as f:
        content = f.readlines()
        data = [x.strip().split('=') for x in content if '=' not in x and not x.startswith('#')]
    secrets = []
    for key in data:
        secrets.append({"name":str(key[0]),"valueFrom":f"${{SECRET_ARN}}:{str(key[0])}::"})
    return list(secrets)

if __name__ == "__main__":
    # python taskdef.py | jq
    containerDefinitions = {
        "essential": True,
        "name": "$APPLICATION_NAME",
        "image": "<IMAGE1_NAME>",
        "environment": convert_env_to_json(),
        "secrets": convert_secret_to_json()
        }
    print(json.dumps(dict(containerDefinitions)))
