import boto3

def lambda_handler(event, context):
 
    id_vuelo = event['id_vuelo']
    id_aerolinea = event['id_aerolinea']
    codigo_vuelo = event['codigo_vuelo']
    origen = event['origen']
    destino = event['destino']
    fecha_salida = event['fecha_salida']
    fecha_llegada = event['fecha_llegada']
    capacidad = event['capacidad']


    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('t_vuelo')  


    vuelo = {
        'id_vuelo': id_vuelo,
        'id_aerolinea': id_aerolinea,
        'codigo_vuelo': codigo_vuelo,
        'origen': origen,
        'destino': destino,
        'fecha_salida': fecha_salida,
        'fecha_llegada': fecha_llegada,
        'capacidad': capacidad
    }


    response = table.put_item(Item=vuelo)

    # Retornar una respuesta exitosa
    return {
        'statusCode': 200,
        'body': 'Vuelo creado con éxito'
    }
