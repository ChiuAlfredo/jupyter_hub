import os
import sys
import shutil

docker_personal_network_folder=os.environ.get('DOCKER_PERSONAL_NETWORK_FOLDER')
docker_shared_network_folder=os.environ.get('DOCKER_SHARED_NETWORK_FOLDER')
host_personal_network_folder=os.environ.get('HOST_PERSONAL_NETWORK_FOLDER')
host_shared_network_folder=os.environ.get('HOST_SHARED_NETWORK_FOLDER')

c.JupyterHub.spawner_class = 'dockerspawner.DockerSpawner'
c.DockerSpawner.network_name = os.environ['DOCKER_NETWORK_NAME']

# Spawn containers from this image
c.DockerSpawner.container_image = os.environ['DOCKER_NOTEBOOK_IMAGE']

# Connect containers to this Docker network
network_name = os.environ['DOCKER_NETWORK_NAME']
c.DockerSpawner.use_internal_ip = True
c.DockerSpawner.network_name = network_name
c.DockerSpawner.extra_host_config = {'runtime': 'nvidia'}
c.Spawner.environment = {'GRANT_SUDO': 'yes'}
c.Spawner.default_url = '/lab'


# c.DockerSpawner.allowed_images = {
#     "tensorflow-cpu": "tensorflow-notebook",
#     "tensorflow-gpu (Tensorflow 2.8)": "tensorflow-notebook",
#     "pytorch-gpu (Pytorch 1.10)": "pytorch-notebook"
# }
# c.DockerSpawner.remove_containers = True




#指定admin為管理者帳號；設定使用FirstUseAuthenticator，我們直接使用內建的帳號管理系統，從admin介面新增使用者之後，使用者在第一次登入時必須自行設定密碼。

from jupyter_client.localinterfaces import public_ips
c.JupyterHub.hub_ip = public_ips()[0]
c.JupyterHub.admin_access = True
c.Authenticator.admin_users = {'admin'}

c.JupyterHub.authenticator_class = 'firstuseauthenticator.FirstUseAuthenticator'
c.LocalAuthenticator.create_system_users = True


# 設定多久刪除環境

#shutdown the server after no activity for an hour
c.ServerApp.shutdown_no_activity_timeout = 60 * 60
#shutdown kernels after no activity for 30 minutes
c.MappingKernelManager.cull_idle_timeout = 30 * 60
#check for idle kernels every two minutes
c.MappingKernelManager.cull_interval = 2 * 60




# 設定建立新使用者的家目錄，並且與docker外的本機目錄連結，家目錄的owner ID/group ID需要與本機的user ID/group ID相同，否則會發生無法編輯的錯誤。

def create_dir_hook(spawner):
   """ Create directory """
   username = spawner.user.name  # get the username
   home_path = os.path.join('/persist/', username)
   if not os.path.exists(home_path):
       os.mkdir(home_path)
       os.chown(home_path, 1000, 1000)  # Same UID/GID as in local machine

c.Spawner.pre_spawn_hook = create_dir_hook
notebook_dir = os.environ.get('DOCKER_NOTEBOOK_DIR') 
c.DockerSpawner.notebook_dir = notebook_dir
c.DockerSpawner.volumes = {'./jupyterhub-data/{username}': notebook_dir}


# JupyterHub的設定與使用者資料會存在/persist下，以免JupyterHub重啟後全部消失。

c.JupyterHub.cookie_secret_file = '/persist/jupyterhub_cookie_secret'
c.JupyterHub.db_url = '/persist/jupyterhub.sqlite'
