FROM node:lts-alpine

WORKDIR /app

COPY package*.json ./

RUN npm install
RUN npm i -g typescript

COPY . .


RUN npm run build

