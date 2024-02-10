# jupyter_hub

建立jupyterhub-data資料夾
```
mkdir jupyterhub-data
```

需配合docker-stakcs使用
```
sudo docker build -t "docker-stacks-foundation" ./docker-stacks/images/docker-stacks-foundation
sudo docker build -t "base-notebook" ./docker-stacks/images/base-notebook
sudo docker build -t "minimal-notebook" ./docker-stacks/images/minimal-notebook
sudo docker build -t "scipy-notebook" ./docker-stacks/images/scipy-notebook
sudo docker build -t "tensorflow-notebook" ./docker-stacks/images/tensorflow-notebook
```

```
docker run -it -p 8888:8888 tensorflow-notebook
```
