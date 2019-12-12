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
    return client.dataset(dataset_id)


def configure_loading_job(isAutoDetect):
    job_config = bigquery.LoadJobConfig()
    job_config.autodetect = isAutoDetect
    job_config.source_format = bigquery.SourceFormat.NEWLINE_DELIMITED_JSON
    return job_config


def load_to_gc_dw(filepath):
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

