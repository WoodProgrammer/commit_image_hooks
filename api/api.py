from flask import Flask,request,abort
from flask_restful import Resource,Api

app = Flask(__name__)
api = Api(app)
images = {}


def image_aborter(image_id):
    abort(404,"Image Not Found")

class DockerApi(Resource):
    def get(self,user_name):
        return images


class DockerImage(Resource):
    def get(self,user_name,image_id):
        try:



            return {user_name:images[user_name][image_id] }

        except:
            print(request)
            image_aborter(image_id)

    def put(self,user_name,image_id):

        data = request.form['status']
        images[image_id] = image_id
        images[image_id] = {}
        images[image_id]['status'] = data


        return {'status':'Saved ! '}

api.add_resource(DockerApi,'/<string:user_name>')
api.add_resource(DockerImage,'/<string:user_name>/<string:image_id>')


if __name__ == '__main__':
    app.run(debug=True)
