FROM nginx:1.26-alpine
RUN apk add --no-cache python3
COPY ./package.json /usr/src/app
WORKDIR /usr/src/app
RUN npm install && npm run build
ENV NODE_ENV=production
COPY .env /usr/src/app/.env
ARG TOKEN=$NODE_ENV.TOKEN
ENV PW=tdw4976bfs290j
USER 1000
CMD ["npm", "start"]
