import pika, os
class Queuer:
    def __init__(self):

        self.url = os.environ.get('CLOUDAMQP_URL', 'amqp://user:password@localhost:5672/%2f')
        self.params = pika.URLParameters(self.url)
        self.connection = pika.BlockingConnection(self.params)
        self.channel = self.connection.channel() # start a channel




    def publisher(self,message):

        self.channel.queue_declare(queue='hello') # Declare a queue
        self.channel.basic_publish(exchange='',
                                  routing_key='hello',
                                  body=message)

        print(" [x] Sent 'Hello World!'")
    def __del__(self):

        self.connection.close()

















'''
docker run -d -p 5672:5672 -p 15672:15672 -p 25672:25672 -p 4369:4369 -e RABBITMQ_DEFAULT_USER=user -e RABBITMQ_DEFAULT_PASS=password rabbitmq:3-management
'''