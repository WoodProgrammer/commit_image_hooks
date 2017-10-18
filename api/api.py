from flask import Flask,request,abort
from flask_restful import Resource,Api
import json
from gitter import Queuer
app = Flask(__name__)
api = Api(app)
images = {}

docker_queue = Queuer()
x = 0
def image_aborter(image_id):
    abort(404,"Image Not Found")

class DockerApi(Resource):
    def get(self,user_name):
        return images


class DockerImage(Resource):
    def get(self,user_name,image_id):
        try:


####db'den çekilecek ....
            return {user_name:images[user_name][image_id] }

        except:
            print(request)
            image_aborter(image_id)

    def put(self,user_name):
        images = {}


        data1 = request.form['branch_name']
        data2 = request.form['repo_name']
        data3 = request.form['git_server']


        images['branch_name'] = data1
        images['repo_name'] = data2
        images['git_server'] = data3

        docker_queue.publisher(json.dumps(images))



        return {'status':'Queued ! '}
    ####bu kisim db'ye atılacak consumer tarafından guncellenecek.

api.add_resource(DockerApi,'/<string:user_name>')
api.add_resource(DockerImage,'/<string:user_name>')


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=7000)
