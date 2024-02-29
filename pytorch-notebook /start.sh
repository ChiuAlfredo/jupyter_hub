#!/bin/bash
# 这里可以包含其他需要在容器启动时执行的命令
# 启动Jupyter Lab，假设你已经安装了Jupyter Lab
jupyter lab --ip='0.0.0.0' --port=7777 --no-browser --allow-root
