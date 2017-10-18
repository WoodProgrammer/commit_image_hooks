import pika, os, git
from builder import Builder
import simplejson as json
image_builder = Builder()


url = os.environ.get('CLOUDAMQP_URL', 'amqp://user:password@localhost:5672/%2f')
params = pika.URLParameters(url)
connection = pika.BlockingConnection(params)
channel = connection.channel() # start a channel

channel.queue_declare(queue='hello')

def docker_builder(ch, method, properties, body):
    tmp  = {}
    tmp = json.loads(body)



    git.Git().clone("git@{}:/home/git/version/{}".format(tmp["git_server"],tmp["repo_name"]),branch=tmp['branch_name'])

        ##BRANCH EKLENEECEK.
        ##DB'DEN QUEUE EXPIRING..(rds)

channel.basic_consume(docker_builder,
                      queue='hello',
                      no_ack=True)

print(' [*] Waiting for messages:')
channel.start_consuming()
