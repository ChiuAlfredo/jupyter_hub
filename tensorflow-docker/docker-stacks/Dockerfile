# 使用Jupyter的基礎Python映像作為起點
FROM tensorflow/tensorflow:latest-gpu-jupyter


# 安装Jupyter Lab
RUN pip install jupyterlab

# 将自定义的启动脚本添加到镜像中
COPY start.sh /usr/local/bin/start.sh

# 使启动脚本可执行
RUN chmod +x /usr/local/bin/start.sh

# 设置容器启动时执行的命令
CMD ["start.sh"]

