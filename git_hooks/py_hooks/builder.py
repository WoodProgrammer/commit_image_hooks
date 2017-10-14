import docker
import os, time
import requests


class Builder:
    def __init__(self):
        self.client = docker.from_env()

    @staticmethod
    def get_docker_file_place():
            real_path = os.getcwd()




    def build_image(self):
        file_path = os.getcwd()
        try:

            image = self.client.images.build(path=self.get_docker_file_place())

            try:
                r = requests.put('http://localhost:5000/emirozbir/{}'.format(image.id), data={"status": "PASSED "})
            except:
                return "ERROR occured while PUT the data to the API "

            return "Image {} builded . hour: {}  date :  {} ".format(image.id, time.strftime("%H:%M:%S"),
                                                                     time.strftime("%d/%m/%Y"))

        except:

            r = requests.put('http://localhost:5000/emirozbir/failed_images/', data={"image":"COMMIT_NUMBER","""status": "FAILED "})
            print r.status_code

            return "Image building attempt failed on last commit  {}".format('hebele')

            ##requestss to the apis


x = Builder()
print(x.build_image())