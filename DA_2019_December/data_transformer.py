#!/usr/bin/python3
"""
    Data Transformation Module
    This module is used to transform the data extracted
    from the API
"""
import json

from loguru import logger


def remove_key(d, key):
    """
        This function is used to remove the key from a python dictionary.
    """
    r = dict(d)
    del r[key]
    return r


def refine_data(extracted_data):
    """
        This function is used to refine the data array
    """
    # allowed_keys = [
    #     "id",
    #     "case_number",
    #     "date",
    #     "block",
    #     "iucr",
    #     "primary_type",
    #     "description",
    #     "location_description",
    #     "arrest",
    #     "domestic",
    #     "beat",
    #     "district",
    #     "ward",
    #     "community_area",
    #     "fbi_code",
    #     "x_coordinate",
    #     "y_coordinate",
    #     "year",
    #     "updated_on",
    #     "latitude",
    #     "longitude",
    #     "location",
    # ]

    restricted = [
        ":@computed_region_awaf_s7ux",
        ":@computed_region_6mkv_f3dw",
        ":@computed_region_vrxf_vc4k",
        ":@computed_region_bdys_3d7i",
        ":@computed_region_43wa_7qmu",
        ":@computed_region_rpca_8um6",
        ":@computed_region_d9mm_jgwp",
        ":@computed_region_d3ds_rm58",
    ]

    refined_list = list()
    selected_keys = list()

    try:
        for d in extracted_data:
            for (key, value) in d.items():
                if key in restricted:
                    selected_keys.append(key)

            # Iterate over the list and delete corresponding key from dictionary
            for key in selected_keys:
                if key in d:
                    del d[key]

            refined_list.append(d)
    except Exception as ex:
        logger.error("Exception during iteration {}".format(ex))

    return refined_list


def write_ndjson(extracted_data):
    """
        This function writes the Newline Delimited JSON data
        to the data folder.
    """
    refined_data = refine_data(extracted_data)
    is_data_written = write_data(refined_data)
    if is_data_written:
        logger.info("JSON ND Conversion Started")
        with open("data/chicago_crime_data.json", "r") as read_file:
            data = json.load(read_file)
        result = [json.dumps(record) for record in data]
        with open("data/chicago_crime_data_nd.json", "w") as obj:
            for i in result:
                obj.write(i + "\n")
        logger.info("ND JSON Conversion Success")
        logger.success(
            "ND JSON Data Written to {} location".format(
                "data/chicago_crime_data_nd.json"
            )
        )
        return True
    else:
        return False


def write_data(refined_data):
    """
        Refining step
        This function is used to transform the extracted data 
        from the endpoint with the proper utf-8 encoding. 
    """
    try:
        with open("data/chicago_crime_data.json", "w", encoding="utf-8") as f:
            logger.info("Prestaging Transformation Started")
            json.dump(refined_data, f, ensure_ascii=False, indent=4)
            logger.info("Transformation Process Ended")
            logger.success(
                "Data Written to {} location".format("data/chicago_crime_data.json")
            )

        return True
    except Exception as ex:
        logger.error("Failed to write data: {}".format(ex))
        return False
