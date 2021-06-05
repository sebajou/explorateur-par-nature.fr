FROM node:14.16.1

WORKDIR /code
COPY package.json .

RUN npm install
RUN npm audit fix
