from utils.queue import Queue
from real_dataclasses import EmailTask

def main():
    
    # Initialize the Queue class with RabbitMQ credentials
    queue = Queue(rmq_url="localhost", rmq_user="admin", rmq_pass="admin")
    email = EmailTask("test@mail.com")
    
    queue.send_task_to_queue(email)
    
if __name__ == "__main__":
    main()
    