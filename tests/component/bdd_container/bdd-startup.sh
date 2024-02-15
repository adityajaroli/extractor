#!/bin/sh

# Setup the Azure Blob Storage. As from our docker-compose.yml file, we have just created an instance of ABS
# For our testing, we need to upload some blob. We will call the utility shared above in the point 5.
python3 component/bdd_container/init_abs.py

# Running test cases
pytest component
