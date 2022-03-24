import os
import logging
import boto3
import botocore
import uuid
import json

from datetime import datetime

logger = logging.getLogger()
logger.setLevel(logging.INFO)

client = boto3.client('dynamodb')

def lambda_handler(event, context):
  
  logger.info('## ENVIRONMENT VARIABLES')
  logger.info(os.environ)
  logger.info('## EVENT')
  logger.info(event)
  
  #Initialize varaiables
  unqiue_id = ""
  request_id = ""
  entry_type = ""
  raw_data = ""
  unique_id = uuid.uuid4()
  
  #check if audit event is for request or response entry
  
  try:
      raw_data = event['finalresponse']['Payload']
      entry_type = 'response'
  except KeyError:
      logger.info('Response object not found in the event!')
      raw_data = event['request']
      entry_type = 'request'
      
  
  #retrieve the request_id from the event payload which is our co-relation id sent from upstream
  
  request_id = event['context']['request_id']
   
  date_obj = datetime.now()
  date_str = date_obj.strftime("%Y-%m-%d %H:%M:%S.%f.%Z")
  
  try:
    data = client.put_item(
      TableName='rule_execution_audit',
      Item={
        'audit_id': {
          'S': str(unique_id)
        },
        'request_id' : {
          'S' : request_id
        },
        'entry_type': {
          'S': entry_type
        },
        'time_stamp': {
          'S': date_str
        },
        'raw_data' :{ 
          'S': str(raw_data)
        }
      }
    )
  except botocore.exceptions.ClientError as e:
        error_string = e.response['Error']['Message']
        logger.error(error_string)
        return populate_response(500, unique_id, error_string)

  return populate_response(200, unique_id, 'successfully created item!')


def populate_response(return_code, trans_id, response_str):
  
  response = {}
  response['StatusCode'] = return_code
  response['trans_id'] = str(trans_id)
  response['body'] = response_str
  response ['headers'] ={}
  response ['headers']['Content-Type'] = 'application/json'
  response ['headers']['Access-Control-Allow-Origin'] = '*'
  logger.info(json.dumps(response))
  return response
  
  
  
