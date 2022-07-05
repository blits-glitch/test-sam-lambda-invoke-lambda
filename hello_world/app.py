import json
import boto3
import os

# import requests


def lambda_handler(event, context):
    env_lambda_name = os.environ['LambdaName']

    print('call caller function')

    # 呼び出し処理
    client = boto3.client('lambda', region_name='ap-northeast-1')
    response = client.invoke(
        FunctionName=env_lambda_name,
        InvocationType='RequestResponse',
        LogType='Tail',
    )

    # bytes型にする
    # 注意：readを一回してしまうとストリームの末尾にシークされてしまうため、2回目以降の呼び出しでは結果を取得できない
    body = response['Payload'].read()

    # utf-8に変換する
    payload = body.decode('utf-8')

    print(payload)

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello world",
            # "location": ip.text.replace("\n", "")
        }),
    }
