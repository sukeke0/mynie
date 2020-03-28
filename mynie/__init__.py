# This file contains the entry_point callable that is responsible for
# dynamically adding the parsers into the Genie framework.

from mynie.parser import linux, myos

__all__ = []

def add_my_parsers():
    """
    See genie/libs/parser/utils/entry_points.py for more information.
    """
    return {
        'linux': [
            linux.free.LinuxFree,
            linux.date.LinuxDate
        ],  
        'myos': [
            myos.free.MyOsFree,
            myos.date.MyOsDate
        ],  
    }
