# Use the specific version of the Ubuntu base image
FROM ubuntu:20.04.5

# Update the package list and install necessary packages
RUN apt-get update && \
    apt-get install -y sysbench

# Set the default command to run sysbench
CMD ["sysbench"]
