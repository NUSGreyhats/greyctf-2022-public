FROM node:16

# Create app directory
WORKDIR /usr/src/app

# Install app dependencies
# A wildcard is used to ensure both package.json AND package-lock.json are copied
# where available (npm@5+)
COPY clumsy-bird/package*.json ./

RUN npm install
RUN npm install -g grunt-cli
# If you are building your code for production
# RUN npm ci --only=production

COPY clumsy-bird .

EXPOSE 8001
CMD [ "grunt", "connect" ]