import boto3

def lambda_handler(event, context):
    source_bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
    
    s3 = boto3.client('s3')
    s3.copy_object(
        Bucket='s3-finish',
        Key=key,
        CopySource={'Bucket': source_bucket, 'Key': key}
    )
    
    return {
        'statusCode': 200,
        'body': 'File copied successfully!'
    }