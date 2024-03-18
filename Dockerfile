FROM nginx:1.19.0-alpine
RUN apk add --no-cache python3
COPY ./package.json /usr/src/app
WORKDIR /usr/src/app
RUN npm install && npm run build
ENV NODE_ENV=production
COPY .env /usr/src/app/.env
ENV TOKEN=$NODE_ENV.TOKEN
ENV PASSWORD=tdw4976bfs290j
CMD ["npm", "start"]
