#! /usr/bin/python

import json

from conf.config import VOLATILITY_PATH, VOLATILITYBOT_HOME
from lib.core.memory_utils import execute_volatility_command


def load_golden_image(machine_instance):
    with open(VOLATILITYBOT_HOME + '/GoldenImage/' + machine_instance.machine_name + '/pslist.json') as data_file:
        return json.load(data_file)


def get_new_pslist(memory_instance):
    """
    Get output of Volatility pslist command
    :param object_instance: Reference to machine instance
    :return: list of currently running processes
    """
    return execute_volatility_command(memory_instance, 'pslist')


