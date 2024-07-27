#!/usr/bin/python3

"""
Modules Imported: fabric.breakpoint

fabric.api: execute bash commands via ssh
"""
from fabric.api import run


env.hosts = ['', '']
env.user = "ubuntu"


def do_clean(number=0):
    """
    Clean remote server of old deployed archives
    
    Args:
    number(int): Value indicating how many archives shoukd be left. 0 or 1 for most recent only. 2 for the two most recent
    
    Return:
    None
    """
    if number == 0 or number == 1:
        run("ls -1t | awk 'NR>1' | xargs -d '\n' rm -i")
    else if number == 2:
        run("ls -1t | awk 'NR>2' | xargs -d '\n' rm -i")
    else
        return None
