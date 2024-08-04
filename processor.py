import pika

def process_data(ch, method, properties, body):
    data = body.decode()
    print(f"Processing data: {data}")

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='data_queue')
channel.basic_consume(queue='data_queue', on_message_callback=process_data, auto_ack=True)

print('Waiting for messages...')
channel.start_consuming()
