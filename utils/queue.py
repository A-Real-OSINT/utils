from pika import BlockingConnection, ConnectionParameters, BasicProperties
from pika.credentials import PlainCredentials as Credentials
from real_dataclasses.tasks.task import Task

class Queue:
    """
    This class implements a simple queue data structure using rabbitmq.
    """
    
    def __init__(self, rmq_url: str, rmq_user: str, rmq_pass: str) -> None:
        """
        Initializes the queue helper.
        :param rmq_url: The URL of the RabbitMQ server.
        :type rmq_url: str
        :param rmq_user: The USERNAME for RabbitMQ authentication.
        :type rmq_user: str
        :param rmq_pass: The PASSWORD for RabbitMQ authentication.
        :type rmq_pass: str
        :return: None
        :rtype: None
        """
        self.rmq_url = rmq_url
         
        self.connection = BlockingConnection(
            ConnectionParameters(
                host=self.rmq_url,
                credentials=Credentials(rmq_user, rmq_pass)
            )
        )
        
        
    
    def send_task_to_queue(self, task:Task) -> None:
        """
        Sends a task to the specified queue.
        :param queue_name: The name of the queue to send the task to.
        :type queue_name: str
        :param task: The task to be sent to the queue.
        :type task: Task
        :return: None
        :rtype: None
        """
        channel = self.connection.channel()
        
        channel.queue_declare(queue=task.task_type, durable=True)
        
        channel.basic_publish(
            exchange='',
            routing_key=task.task_type,
            body=task._json_str(),
            properties=BasicProperties(
                delivery_mode=2,
            )
        )
        
