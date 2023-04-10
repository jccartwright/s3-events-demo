import json


def lambda_handler(event, context):
    # usually only one record
    for sqs_record in event['Records']:
        # JSON SNS message nested within JSON SQS message body
        body = json.loads(sqs_record['body'])
        payload = json.loads(body['Message'])

        # usually only one record
        for record in payload['Records']:
            s3 = record['s3']
            print(s3)
            bucket_name = s3['bucket']['name']
            object_key = s3['object']['key']
            print(f's3://{bucket_name}/{object_key}')


# SQS
# {
#     'Records': [
#         {
#             'messageId': '9ce42eb4-e3c2-4489-bf97-d5f77147a2fe',
#             'receiptHandle': 'AQEBUSfywITDaP7+AV2Jao+81tbJkORuS2vh4JQ28N41Ged/Edef+hJSgv78uz+mai6Oxuf/8KX/c3mTdgAPwft1TCzDJKOFcgcHwD8Pr8Md9FLL9OvSobRQYiJ//FAMHkjh7wBPbXNTUiw48Z3a9uzFJ34WcgjPi8WGLJTodJxmqWmMWh8X+I65pUvEptxst+Xwu9Dfjd5tyl6TAfrdOECJR7Dc6PnTHO0yjcsWCR7niZ0O7AVIp70ZdjS4qfafvx0F7YwVZ4v0eJF6FusisenNNq8pa+0VR1/KUJqJCbs/p04ctJlrPZMlBBeYTmUfKZxt1tTDNfb2xdf6U/a8L/Gjy6y9m6HTWtIgou1BJNdefHP1OgXYjWNKBnkVL9bEgS8+4ulcTiT9OQHgT8IXmKPT0A==',
#             'body': '{\n  "Type" : "Notification",\n  "MessageId" : "30f75bf5-1d60-5f10-82f2-075ef0bc74fe",\n  "TopicArn" : "arn:aws:sns:us-west-2:619726840331:incoming-csb-events-topic",\n  "Subject" : "Amazon S3 Notification",\n  "Message" : "{\\"Records\\":[{\\"eventVersion\\":\\"2.1\\",\\"eventSource\\":\\"aws:s3\\",\\"awsRegion\\":\\"us-west-2\\",\\"eventTime\\":\\"2023-04-08T22:32:59.743Z\\",\\"eventName\\":\\"ObjectCreated:Put\\",\\"userIdentity\\":{\\"principalId\\":\\"AWS:AROAZASUZEIFXOK6VOQWQ:joca5730@colorado.edu\\"},\\"requestParameters\\":{\\"sourceIPAddress\\":\\"198.11.28.46\\"},\\"responseElements\\":{\\"x-amz-request-id\\":\\"REAYTKPQQ8CDNZ69\\",\\"x-amz-id-2\\":\\"yvnLw9/SFXToaIvNhiMmrndNAmmGX0HDe4xSUFE1kWCUSy/BjKUAolAnWPUiEq+UoPT6g4B9d/csjii7yxpDLyW0tnJQsKSE\\"},\\"s3\\":{\\"s3SchemaVersion\\":\\"1.0\\",\\"configurationId\\":\\"03faae6b-91a1-42cd-8fe8-75f3439fcafc\\",\\"bucket\\":{\\"name\\":\\"jcc-incoming-data\\",\\"ownerIdentity\\":{\\"principalId\\":\\"A1D95GOQ3QBL4X\\"},\\"arn\\":\\"arn:aws:s3:::jcc-incoming-data\\"},\\"object\\":{\\"key\\":\\"csb/csv/csb/csv/2023/04/05/20230405164942848807_ac5ff8d4-84be-43fd-9278-58fc93a0abc0_pointData.csv\\",\\"size\\":2441303,\\"eTag\\":\\"b0182dd17762b4efae0ceddad27b85be\\",\\"sequencer\\":\\"006431EB9B9E150DFF\\"}}}]}",\n  "Timestamp" : "2023-04-08T22:33:00.431Z",\n  "SignatureVersion" : "1",\n  "Signature" : "WCyxY9t3uXtJGiKzW6VZlKQHVDN3IqgzAcY7yew1jO+9ybn0usx03Rp7V5Mv+DL5I3w/qP6PQj/pU7KAzkGFQHyXyf3wyiiMrtUBXKrTgY8ibWO0rGNq9UjX9F73c449h9x9CFmby/16u3bIXc0YcCP3JhTbt0+8NcqOPgbv174X2jrCrPAMdOk1wyWQUclqp+Yjrb6u3I3zFKMDmpcjrFSJT77XyXK/M+e8bOcXiuxgVkfWufZN2Np2yzDUBMpKVZshiRXIVwNsvsiQzhM1biJH4ugETfAMCHcRs3HDo91fUMU8SqgJx9OvIwQhmJ8WPEDaRLGzt/VgXwDeFhBAsQ==",\n  "SigningCertURL" : "https://sns.us-west-2.amazonaws.com/SimpleNotificationService-56e67fcb41f6fec09b0196692625d385.pem",\n  "UnsubscribeURL" : "https://sns.us-west-2.amazonaws.com/?Action=Unsubscribe&SubscriptionArn=arn:aws:sns:us-west-2:619726840331:incoming-csb-events-topic:a6ab4192-67bd-48d8-b315-f2b84d133eac"\n}',
#             'attributes': {
#                 'ApproximateReceiveCount': '1',
#                 'SentTimestamp': '1680993180498',
#                 'SenderId': 'AIDAIYLAVTDLUXBIEIX46',
#                 'ApproximateFirstReceiveTimestamp': '1680993180508'
#             },
#             'messageAttributes': {},
#             'md5OfBody': '8c9e428bacc7acda0f36639aac2c7374',
#             'eventSource': 'aws:sqs',
#             'eventSourceARN': 'arn:aws:sqs:us-west-2:619726840331:incoming-csb-file-queue',
#             'awsRegion': 'us-west-2'
#         }
#     ]
# }

# SNS Message
# {
# 	"Records": [{
# 		"eventVersion": "2.1",
# 		"eventSource": "aws:s3",
# 		"awsRegion": "us-west-2",
# 		"eventTime": "2023-04-08T22:54:18.880Z",
# 		"eventName": "ObjectCreated:Put",
# 		"userIdentity": {
# 			"principalId": "AWS:AROAZASUZEIFXOK6VOQWQ:joca5730@colorado.edu"
# 		},
# 		"requestParameters": {
# 			"sourceIPAddress": "198.11.28.46"
# 		},
# 		"responseElements": {
# 			"x-amz-request-id": "KK722DE5PN7KT2V1",
# 			"x-amz-id-2": "W2fPlN83dUySamkzw0wEQ0iO3csIobA1qw0EFftMbN03EYQCWxesGJ7viIDhqAv4kUXqox2Rg84ocIY2JH0YujHeZQSEIaWY"
# 		},
# 		"s3": {
# 			"s3SchemaVersion": "1.0",
# 			"configurationId": "03faae6b-91a1-42cd-8fe8-75f3439fcafc",
# 			"bucket": {
# 				"name": "jcc-incoming-data",
# 				"ownerIdentity": {
# 					"principalId": "A1D95GOQ3QBL4X"
# 				},
# 				"arn": "arn:aws:s3:::jcc-incoming-data"
# 			},
# 			"object": {
# 				"key": "csb/csv/.DS_Store",
# 				"size": 6148,
# 				"eTag": "b72b9c8264cd17d163a8ddcf3caa4b58",
# 				"sequencer": "006431F09AD79544B5"
# 			}
# 		}
# 	}]
# }
