import docker
import os, time
import requests


class Builder:
    def __init__(self):
        self.client = docker.from_env()



    def build_image(self,path=None,tag=''):
        try:
            image = self.client.images.build(path=path,tag=tag)
            return True

        except:
            return False
x = Builder()
data = x.build_image(path='.',tag='hablela')



