#!/usr/bin/python3

"""
Modules Imported: datetime

datetime: Package conatins several modules to track and return time
(even timezones). Used to get current time when script is executed
"""
from datetime import datetime


def do_pack():
    """"
    Generates a .tgz archive from the contents of ./web_static/ dir using 
    fabric

    Attributes:
    None

    Return:
    Path to the archive if successful, otherwise None
    """
    time = datetime.now
    time_string = f"{time.year_time.month_time.day_time.hour_time.minute_time.second}"
    tar_file = run(f"mkdir ./versions && tar -cvf 
            ./versions/web_static_{time_string}.tar.gz ./web_static/*")
    if tar_file.succeded:
        return tar_file.path() ###
    else:
        return None
