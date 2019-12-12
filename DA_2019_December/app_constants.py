#!/usr/bin/python3
"""
    Constants of the application
"""
import os

from dotenv import load_dotenv

# Get the path to the directory this file located in
BASEDIR = os.path.abspath(os.path.dirname(__file__))
# Connecting the path with our '.env' file name
load_dotenv(os.path.join(BASEDIR, "../.env"))

###########################################################################################
##################################### App Constants #######################################
###########################################################################################

# Socrata service parameters of Chicago crime data
so_sandbox = os.getenv("SO_SANDBOX")
so_identifier = os.getenv("SO_DATASET_IDENTIFIER")

# Socrata account credentials.
api_token = os.getenv("SO_API_TOKEN")
username = os.getenv("SO_EMAIL")
password = os.getenv("SO_PASSWORD")

# Limit of the data to be extracted
max_data_limit = os.getenv("MAX_DATA_LIMIT")

# Our unique dataset ids
gc_dataset_id = os.getenv("GC_DATASET_ID")
gc_table_id = os.getenv("GC_TABLE_ID")
