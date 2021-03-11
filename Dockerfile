FROM python:3.8.5

RUN apt-get update

COPY backend/requirements.txt $HOME
RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt