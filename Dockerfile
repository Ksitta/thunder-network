FROM nikolaik/python-nodejs:python3.8-nodejs12

RUN apt-get update

RUN npm config set registry https://registry.npm.taobao.org

ENV FRONTEND=/opt/frontend

WORKDIR $FRONTEND

COPY frontend/package.json $FRONTEND
COPY frontend/package-lock.json $FRONTEND
RUN npm install

COPY frontend/ $FRONTEND
RUN npm run build

ENV HOME=/opt/app
WORKDIR $HOME

COPY backend/requirements.txt $HOME
RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt

COPY backend $HOME/backend
# COPY config $HOME/config

RUN cp -r /opt/frontend $HOME/frontend

EXPOSE 8000
ENV NUXT_PORT=8000
ENV NUXT_HOST=0.0.0.0

ENV PYTHONUNBUFFERED=true