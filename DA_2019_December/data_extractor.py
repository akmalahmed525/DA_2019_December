#!/usr/bin/python3
"""
    Data Extraction Module
    This module is used to extract the data from the API
"""
from app_constants import *

from loguru import logger
from sodapy import Socrata


# Socrata object
so_client = Socrata(so_sandbox, api_token, username=username, password=password)


def extract_data():
    """
        This function is used to extract the data from
        the endpoint.
    """
    try:
        logger.info("Data Extraction Started")
        results = so_client.get(so_identifier, limit=int(max_data_limit))
        logger.success("Data Extraction Success")
        return results
    except Exception as ex:
        logger.error("An Error Occured while extracting data: {}".format(ex))
        return []
