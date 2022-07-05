import json

# import requests


def lambda_handler(event, context):
    print('called by other lambda')

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello world",
            "message2": "Good Morning"
            # "location": ip.text.replace("\n", "")
        }),
    }
