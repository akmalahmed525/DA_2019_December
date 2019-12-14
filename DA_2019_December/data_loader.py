#!/usr/bin/python3
"""
    Data Loader Module
    This module will load the data to our BigQuery DW
"""
from loguru import logger
from google.cloud import bigquery
from app_constants import *

# Defining the client.
client = bigquery.Client()


def get_dataset_reference(dataset_id):
    """
        This function is used to get the dataset reference
        from the BigQuery Data Warehouse.
    """
    return client.dataset(dataset_id)


def configure_loading_job(isAutoDetect):
    """
        This function is used to configure the data loading job.
    """
    # Initiating the loading job
    job_config = bigquery.LoadJobConfig()
    
    # Auto detecting the schema based on the default JSON object.
    job_config.autodetect = isAutoDetect

    # We define the data source format as
    # Newline Delimited JSON objects
    # 
    # eg:-
    #
    # JSON Array Format
    # [
    #   { 'name': 'User1', 'ref': '24c9e15e52afc47c225b757e7bee1f9d' },
    #   { 'name': 'User2', 'ref': '7e58d63b60197ceb55a1c487989a3720' }    
    # ]
    #
    # Newline Delimited JSON Object Format
    #
    # { 'name': 'User1', 'ref': '24c9e15e52afc47c225b757e7bee1f9d' }
    # { 'name': 'User2', 'ref': '7e58d63b60197ceb55a1c487989a3720' }
    #
    job_config.source_format = bigquery.SourceFormat.NEWLINE_DELIMITED_JSON
    return job_config


def load_to_gc_dw(filepath):
    """
        This function is used to load the data
        to the Data Warehouse.
    """
    logger.info("Loading to Warehouse Started")
    dataset_ref = get_dataset_reference(gc_dataset_id)
    table_ref = dataset_ref.table(gc_table_id)
    job_config = configure_loading_job(True)
    try:
        with open(filepath, "rb") as source_file:
            job = client.load_table_from_file(
                source_file, table_ref, job_config=job_config
            )

        job.result()  # Waits for table load to complete.
        logger.success(
            "Loaded {} rows into {}:{}.".format(
                job.output_rows, gc_dataset_id, gc_table_id
            )
        )
        return True
    except Exception as ex:
        logger.error("Loading Exception: {}".format(ex))
        return False

