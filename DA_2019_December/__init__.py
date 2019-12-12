#!/usr/bin/python3
"""
    __init__.py

    The entrypoint of the application.
"""
import os

from loguru import logger
from data_extractor import extract_data
from data_transformer import write_ndjson
from data_loader import load_to_gc_dw

if __name__ == "__main__":
    """
       Main entrypoint of the module. 
    """
    try:
        # Extraction
        extracted_data = extract_data()
        if len(extracted_data) > 0:
            # Transformation
            is_file_written = write_ndjson(extracted_data)
            if is_file_written:
                # Loading
                root_path = os.path.abspath(os.path.dirname(__file__))
                relative_path = "../data/chicago_crime_data_nd.json"
                absolute_file_path = os.path.join(root_path, relative_path)

                # The loading process yet to begin.
                has_data_loaded = load_to_gc_dw(absolute_file_path)
                logger.debug(
                    "Data successfully loaded."
                    if has_data_loaded
                    else "Data loading to Warehouse failed"
                )
            else:
                logger.error("Failed to write the data.")
        else:
            logger.error("Failed to extract the data, please try again.")
    except Exception as ex:
        logger.error("Exception occurred during the prestaging")
    finally:
        logger.debug("Process Finished")
