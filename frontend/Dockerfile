FROM node:14.16.1

#RUN adduser myuser
#USER myuser

WORKDIR /code
COPY package.json .

RUN npm install
RUN npm audit fix
