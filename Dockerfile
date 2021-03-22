FROM node:12.18.3

RUN apt-get update

RUN npm config set registry https://registry.npm.taobao.org

ENV FRONTEND=/opt/frontend

WORKDIR $FRONTEND

COPY frontend/package.json $FRONTEND
COPY frontend/package-lock.json $FRONTEND
RUN npm install
COPY frontend/ $FRONTEND
RUN npm run build

FROM python:3.8.5

ENV HOME=/opt/app
WORKDIR $HOME

COPY backend/requirements.txt $HOME
RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt

COPY backend $HOME/backend

EXPOSE 80
ENV NUXT_PORT=80
ENV NUXT_HOST=0.0.0.0

ENV PYTHONUNBUFFERED=true
