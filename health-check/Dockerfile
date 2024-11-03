# Use Ubuntu as the base image
FROM ubuntu:20.04

# Install required packages
RUN apt-get update && \
    apt-get install -y --no-install-recommends curl bash && \
    rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /usr/src/app

# Copy the health check script into the container
COPY health-check-script.sh .

# Make the script executable
RUN chmod +x health-check-script.sh

# Set the command to run the health check script
CMD ["./health-check-script.sh"]

