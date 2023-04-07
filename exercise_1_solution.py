"""
Exercise: Python Coding
Objective:
Define functions that can apply a filter to supplied data
Notes:
Candidate can rename functions, create new ones as much as they want.
Candidate can import additional packages/modules if need be.
Candidate can change function definition if required.
"""

import logging

ACCEPT = "Accept"
DECLINE = "Decline"
REFER = "Refer"
EXPERIAN = "Experian"
TRANSUNION = "Transunion"
EQUIFAX = "Equifax"

data_sample: list = [
    {
        "Key": "A001",
        "Result": ACCEPT,
        "Service": EQUIFAX
    },
    {
        "Key": "A002",
        "Result": DECLINE,
        "Service": EQUIFAX
    },
    {
        "Key": "A003",
        "Result": ACCEPT,
        "Service": EQUIFAX
    },
    {
        "Key": "A004",
        "Result": REFER,
        "Service": EQUIFAX
    },
    {
        "Key": "A005",
        "Result": REFER,
        "Service": EQUIFAX
    },
    {
        "Key": "A006",
        "Result": DECLINE,
        "Service": EQUIFAX
    }
]


def get_matching_entries(data_list: list, dict_key: str, dict_value: str):
    """Function that applies a filter for the data entries.
    Returns all items that match the filter
    :param data_list: A list of dictionary values
    :type data_list: list
    :param dict_key: The matching key
    :type dict_key: string
    :returns dict_value: The matching filter
    :type dict_value: string
    """
    filter_list: list = []
    try:
        filter_list = [d for d in data_list if d[dict_key] is dict_value]
        logging.info('Retrieve the list data that matches key and result values.')
    except KeyError:
        logging.error('Value not found.')
    return filter_list


def get_non_matching_entries(data_list: list, dict_key: str, dict_value: str):
    """Function that applies a filter for the data entries.
    Returns all items that do not match the filter
    :param data_list: A list of dictionary values
    :type data_list: list
    :param dict_key: The matching key
    :type dict_key: string
    :returns dict_value: The matching filter
    :type dict_value: string
    """
    filter_list: list = []
    try:
        filter_list = [d for d in data_list if d[dict_key] is not dict_value]
        logging.info('Retrieve the list data that does not match key and result values.')
    except KeyError:
        logging.error('Value not found.')
    return filter_list
