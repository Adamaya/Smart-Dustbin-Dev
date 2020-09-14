import json
import boto3
import cgi, json
from botocore.config import Config


def lambda_handler(event, context):
    my_config = Config(
        region_name='ap-south-1',
        signature_version='v4',
        retries={
            'max_attempts': 10,
            'mode': 'standard'
        }
    )

    client = boto3.client('dynamodb', config=my_config, aws_access_key_id='AKIAVTZV5EKIRX7QEHW4',
                          aws_secret_access_key='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')

    bins = ['dustbin_1', 'dustbin_2', 'dustbin_3', 'dustbin_4']
    complete_bins_details = {}
    bin_details_1, bin_details_2, bin_details_3, bin_details_4, = {}, {}, {}, {}

    for bin_id in bins:
        response = client.get_item(
            TableName='dustbins_live_status',
            Key={
                'dustbin_id': {"S": bin_id}
            }
        )
        if bin_id == 'dustbin_1':
            bin_details_1['dustbin_id'] = response['Item']['dustbin_id']['S']
            bin_details_1['date'] = response['Item']['date']['S']
            bin_details_1['time'] = response['Item']['time']['S']
            bin_details_1['latitude'] = response['Item']['latitude']['S']
            bin_details_1['longitude'] = response['Item']['longitude']['S']
            bin_details_1['sweeper_contact_no'] = response['Item']['sweeper_contact_no']['S']
            bin_details_1['sweeper_name'] = response['Item']['sweeper_name']['S']
            bin_details_1['sensor_value'] = response['Item']['sensor_value']['S']
            complete_bins_details[bin_id] = bin_details_1

        elif bin_id == 'dustbin_2':
            bin_details_2['dustbin_id'] = response['Item']['dustbin_id']['S']
            bin_details_2['date'] = response['Item']['date']['S']
            bin_details_2['time'] = response['Item']['time']['S']
            bin_details_2['latitude'] = response['Item']['latitude']['S']
            bin_details_2['longitude'] = response['Item']['longitude']['S']
            bin_details_2['sweeper_contact_no'] = response['Item']['sweeper_contact_no']['S']
            bin_details_2['sweeper_name'] = response['Item']['sweeper_name']['S']
            bin_details_2['sensor_value'] = response['Item']['sensor_value']['S']
            complete_bins_details[bin_id] = bin_details_2

        elif bin_id == 'dustbin_3':
            bin_details_3['dustbin_id'] = response['Item']['dustbin_id']['S']
            bin_details_3['date'] = response['Item']['date']['S']
            bin_details_3['time'] = response['Item']['time']['S']
            bin_details_3['latitude'] = response['Item']['latitude']['S']
            bin_details_3['longitude'] = response['Item']['longitude']['S']
            bin_details_3['sweeper_contact_no'] = response['Item']['sweeper_contact_no']['S']
            bin_details_3['sweeper_name'] = response['Item']['sweeper_name']['S']
            bin_details_3['sensor_value'] = response['Item']['sensor_value']['S']
            complete_bins_details[bin_id] = bin_details_3

        elif bin_id == 'dustbin_4':
            bin_details_4['dustbin_id'] = response['Item']['dustbin_id']['S']
            bin_details_4['date'] = response['Item']['date']['S']
            bin_details_4['time'] = response['Item']['time']['S']
            bin_details_4['latitude'] = response['Item']['latitude']['S']
            bin_details_4['longitude'] = response['Item']['longitude']['S']
            bin_details_4['sweeper_contact_no'] = response['Item']['sweeper_contact_no']['S']
            bin_details_4['sweeper_name'] = response['Item']['sweeper_name']['S']
            bin_details_4['sensor_value'] = response['Item']['sensor_value']['S']
            complete_bins_details[bin_id] = bin_details_4

    final_response = json.dumps(complete_bins_details)

    return json.loads(final_response)
