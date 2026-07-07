# Use the official Node.js 20 image
FROM node:20-alpine

# Create the application directory
WORKDIR /app

# Copy dependency files
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the rest of the application
COPY . .

# Expose the application port
EXPOSE 3001

# Start the application
CMD ["npm", "start"]