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
            return True,image

        except:
            return False