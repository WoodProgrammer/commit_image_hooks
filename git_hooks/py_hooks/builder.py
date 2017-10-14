import docker
import os,time

class Builder:
    docker_path = lambda path: path.split("/")
    def __init__(self):
        self.client = docker.from_env()

    def build_image(self):
        file_path = self.docker_path(os.getcwd())
        try:
            image = self.client.build(path = file_path[5])
            return "Image {} builded . hour: {}  date :  {} ".format(image.id,time.strftime("%H:%M:%S"),time.strftime("%d/%m/%Y"))
        except:
            return "Image building attempt failed on last commit  {}".format()


            ##requestss to the apis



