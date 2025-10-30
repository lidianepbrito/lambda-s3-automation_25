import json

def lambda_handler(event, context):
    print("Evento recebido:", json.dumps(event, indent=2))
    for record in event['Records']:
        bucket_name = record['s3']['bucket']['name']
        file_name = record['s3']['object']['key']
        print(f"Arquivo recebido: {file_name} no bucket: {bucket_name}")
    return {
        'statusCode': 200,
        'body': json.dumps('Função Lambda executada com sucesso!')
    }
