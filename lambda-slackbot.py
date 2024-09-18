from datetime import datetime

def lambda_handler(event, context):
    import subprocess
    slackhook = "https://hooks.slack.com/triggers/XXXXXX/XXXXXX"
    data = "{\"date\":\"" + str(datetime.today().strftime('%Y%m%d')) + "\"}"
    result = subprocess.call(f'curl -X POST -H "Content-type:application/json" --data {data} {slackhook}', shell=True)
    return result
