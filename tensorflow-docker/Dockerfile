# 使用Jupyter的基礎Python映像作為起點
FROM tensorflow/tensorflow:latest-gpu-jupyter

# 安裝JupyterLab
RUN pip install jupyterlab

# 設定啟動時執行JupyterLab
CMD ["start.sh", "jupyter", "lab"]