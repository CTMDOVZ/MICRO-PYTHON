import boto3

def lambda_handler(event, context):

    id_aerolinea = event['id_aerolinea']
    nombre = event['nombre']
    codigo = event['codigo']
    pais_origen = event['pais_origen']


    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('t_aerolineas') 


    aerolinea = {
        'id_aerolinea': id_aerolinea,
        'nombre': nombre,
        'codigo': codigo,
        'pais_origen': pais_origen
    }


    response = table.put_item(Item=aerolinea)


    return {
        'statusCode': 200,
        'body': 'Aerolínea creada con éxito'
    }
