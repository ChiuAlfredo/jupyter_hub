import os
 import sys
 import shutil
 
 c.JupyterHub.spawner_class = 'dockerspawner.DockerSpawner'
 c.DockerSpawner.network_name = os.environ['DOCKER_NETWORK_NAME']
 
 c.DockerSpawner.allowed_images = {
     "tensorflow-cpu": "jupyter/tensorflow-notebook",
     "tensorflow-gpu (Tensorflow 2.8)": "harbor.aif.tw/env/tensorflow-notebook",
     "pytorch-gpu (Pytorch 1.10)": "harbor.aif.tw/env/pytorch-notebook"
 }
 c.DockerSpawner.remove_containers = True
 c.DockerSpawner.extra_host_config = {'runtime': 'nvidia'}
 c.Spawner.environment = {'GRANT_SUDO': 'yes'}
 c.Spawner.default_url = '/lab'
