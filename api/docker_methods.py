import docker,os
import requests
class DockerMethods:
    def __init__(self):
        self.cli = docker.from_env()
        path = os.getcwd()
        docker_file_splitter = lambda  p: p.split('/')
        self.dockerfile_path = docker_file_splitter(path)


    def build(self):
        self.cli.images.build(path=self.dockerfile_path)

        try:
            r = requests.put('http://localhost:5000/emirozbir/todo42', data={"data": "val"})
        except:
            return "ERROR ON NETWORK TO API"