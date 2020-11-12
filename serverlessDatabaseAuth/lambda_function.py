import boto3

s3 = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')
        
def lambda_handler(event, context):
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
    
    obj = s3.get_object(Bucket = bucket, Key = key)
    
    rows = obj['Body'].read().split('\n')
       
    table = dynamodb.Table('newcondition')   
    
    with table.batch_writer() as batch:
        for row in rows:
            batch.put_item(Item={
                'Timestamp' :row.split(',')[0],
                'L_1' :row.split(',')[1],
                'L_2' :row.split(',')[2],
                'A_1' :row.split(',')[3],
                'A_2' :row.split(',')[4],
                'B_1' :row.split(',')[5],
                'B_2' :row.split(',')[6],
                'C_1' :row.split(',')[7],
                'C_2' :row.split(',')[8],
                'A_3' :row.split(',')[9],
                'A_4' :row.split(',')[10],
                'B_3' :row.split(',')[11],
                'B_4' :row.split(',')[12],
                'C_3' :row.split(',')[13],
                'C_4' :row.split(',')[14],
                'L_3' :row.split(',')[15],
                'L_4' :row.split(',')[16],
                'L_5' :row.split(',')[17],
                'L_6' :row.split(',')[18],
                'L_7' :row.split(',')[19],
                'L_8' :row.split(',')[20],
                'L_9' :row.split(',')[21],
                'L_10' :row.split(',')[22],
                'A_5' :row.split(',')[23],
                'B_5' :row.split(',')[24],
                'C_5' :row.split(',')[25]
            })