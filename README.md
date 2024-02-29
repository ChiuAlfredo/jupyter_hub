# jupyter_hub

建立jupyterhub-data資料夾
```
mkdir jupyterhub-data
```
需配合docker-stakcs使用
```
<!-- sudo docker build -t "docker-stacks-foundation" ./docker-stacks/images/docker-stacks-foundation
sudo docker build -t "base-notebook" ./docker-stacks/images/base-notebook
sudo docker build -t "minimal-notebook" ./docker-stacks/images/minimal-notebook
sudo docker build -t "scipy-notebook" ./docker-stacks/images/scipy-notebook
sudo docker build -t "tensorflow-notebook" ./docker-stacks/images/tensorflow-notebook -->

sudo docker build -t "tensorflow-notebook" ./tensorflow-notebook
sudo docker build -t "pytorch-notebook" ./pytorch-notebook
```

<!-- ```
docker run --gpus all -it -p 8888:8888 tensorflow-notebook
docker run --gpus all -it -p 7777:8888 pytorch-notebook
``` -->
# 啟動jupyterhub
```
docker-compose build
docker-compose up -d
```
```
from tensorflow.python.client import device_lib

# 列出所有的本地机器设备
local_device_protos = device_lib.list_local_devices()
# 打印
print(local_device_protos)
```
