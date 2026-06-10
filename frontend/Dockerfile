FROM node:20-alpine

WORKDIR /app

# get dependencies
COPY package.json package-lock.json* ./
RUN npm install

# copy everything
COPY . .

CMD ["npm", "run", "dev", "--", "--host"]