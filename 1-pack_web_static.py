#!/usr/bin/python3
# To be used with fab command to archive web_static/ dir files

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
    time_string = f"{time.year}{time.month}{time.day}\
{time.hour}{time.minute}{time.second}"
    tar_file = run(f"mkdir ./versions && tar -cvf\
 ./versions/web_static_{time_string}.tgz ./web_static/*")
    if tar_file.succeded:
        tar_file.stdout
        return f"./versions/web_static/web_static_{time_string}"  # return path
    else:
        return None
