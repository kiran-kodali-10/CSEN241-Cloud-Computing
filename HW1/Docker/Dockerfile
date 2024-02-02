# Use your custom sysbench image
FROM ubuntu-arm-sysbench

# Copy scripts
COPY tests-script.sh /tests-script.sh

# Set execution permissions for the scripts
RUN chmod +x /tests-script.sh

# Set the entry point
ENTRYPOINT ["/bin/bash","/tests-script.sh"]
