import docker
import os, time
import requests


class Builder:
    def __init__(self):
        self.client = docker.from_env()

    def get_docker_file_place(self,path=None):
        if path is None:
            file_path = os.getcwd().split('/')
            file_path.pop()
            file_path.pop()

            return '/'.join(file_path)
        else:
            return path

    def build_image(self):

        try:

            image = self.client.images.build(path=self.get_docker_file_place())

            try:
                r = requests.put('http://localhost:5000/{}'.format('project_1'), data={"status": "BUILT "})
                return "POSTED" + str(r.status_code)
            except:
                return "ERROR occured while PUT the data to the API "

            return "Image {} builded . hour: {}  date :  {} ".format(image.id, time.strftime("%H:%M:%S"),
                                                                     time.strftime("%d/%m/%Y"))

        except:

            r = requests.put('http://localhost:5000/{}'.format('project_1'), data={"status": "NOT BUILD "})
            print r.status_code

            return "Image building attempt failed on last commit  {}".format('hebele')

            ##requestss to the apis

