import pika
import time
from pika import BlockingConnection, ConnectionParameters
from pika.credentials import PlainCredentials as Credentials

connection = BlockingConnection(
            ConnectionParameters(
                host="localhost",
                credentials=Credentials("admin", "admin")
            )
        )
channel = connection.channel()

channel.queue_declare(queue='email', durable=True)
print(' [*] Waiting for messages. To exit press CTRL+C')


def callback(ch, method, properties, body):
    print(f" [x] Received {body.decode()}")
    time.sleep(body.count(b'.'))
    print(" [x] Done")
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='email', on_message_callback=callback)

channel.start_consuming()