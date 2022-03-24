import json
import logging
import requests
import os
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

def lambda_handler(event, context):
    
    logger.info('## ENVIRONMENT VARIABLES')
    logger.info(os.environ)
    logger.info('## EVENT')
    logger.info(event)
    response = ""
    headers= {"Content-Type": "application/json", "Accept":"*/*"} 
    
    input_data = {}
    input_data = event['request']
    trans_id = event['audit']['Payload']['trans_id']
    
    logger.info('## INPUT ##')
    logger.info(input_data)
    
    url = os.environ['DROOLS_URL'];    
    if url is not None:
        try :
            response = requests.post(url, headers=headers, json=input_data)
            print("Status Code", response.status_code)
            response_str = response.json()
            logger.info('## JSON Response from drools engine ##')
            logger.info(response_str)
        except ConnectionError as e:
            # manage connection errors 
            error_string = e.response['Error']['Message']
            logger.error(error_string)
            return populate_response(500, unique_id, error_string)
        except requests.exceptions.RequestException as err:
            # manage requests errors
            error_string = e.response['Error']['Message']
            logger.error(error_string)
            return populate_response(500, unique_id, error_string)
    else:
        error_string = 'DROOLS_URL environment variable not defined'
        logger.error(error_string)
        return populate_response(500, unique_id, error_string)
        
    return populate_response(200, trans_id, response_str)

def populate_response(return_code, trans_id, response_str):
  
  response = {}
  response['StatusCode'] = return_code
  response['trans_id'] = str(trans_id)
  response['body'] = response_str
  response ['headers'] ={}
  response ['headers']['Content-Type'] = 'application/json'
  response ['headers']['Access-Control-Allow-Origin'] = '*'
  logger.info('##Lambda Response##')
  logger.info(json.dumps(response))
  return response
