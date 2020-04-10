# coding: utf-8
event={'Records': [{'eventVersion': '2.1', 'eventSource': 'aws:s3', 'awsRegion': 'us-east-1', 'eventTime': '2020-04-10T16:39:01.436Z', 'eventName': 'ObjectCreated:Put', 'userIdentity': {'principalId': 'AWS:AIDAJYDZINUY6VBO4CP2E'}, 'requestParameters': {'sourceIPAddress': '100.8.182.126'}, 'responseElements': {'x-amz-request-id': 'A96AC4D5B8BEDD03', 'x-amz-id-2': 'Debm9pRdV8P1tyQdIR/g65SSdBnMR+HC2zk72ibACRqtfL+07HfI8qru2Wu3wCbAgWK7rQiVtJphwN7+orA7Y9dpnzH9Ww1f'}, 's3': {'s3SchemaVersion': '1.0', 'configurationId': '868b022d-430e-4273-a236-6affd2c066a7', 'bucket': {'name': 'videolyzer-navid1', 'ownerIdentity': {'principalId': 'A3BSVOAIQGUYXK'}, 'arn': 'arn:aws:s3:::videolyzer-navid1'}, 'object': {'key': 'Pexels+Videos+3653.mp4', 'size': 7991476, 'eTag': 'd08065a5271404c7e774bcc7640955ab', 'sequencer': '005E90A126522CB071'}}}]}
event
event.keys
event.keys()
event['Records'][0]['s3']['bucket']['name']
event['Records'][0]['s3']['object']['key']
import urllib
urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'])
get_ipython().run_line_magic('save', '1-15')
get_ipython().run_line_magic('save', '1-15 s3-event-example.py')
get_ipython().run_line_magic('save', 's3-event-example.py 1-15')
