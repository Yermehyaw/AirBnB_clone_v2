#!/usr/bin/python3

"""
Modules Imported: fabric.api, os.path.exists, 1-pack_wrb_static,
2-do_deploy_web_static

fabric.api: code deployment tools via ssh
ssh.exists: checks if a file exists
1-pack_web_static.do_pack: creates a .tgz archive of code to ve deplyed to the
server. Returns the path to the archive as a string
2-do_deploy_web_static.do_deploy: a func that drlpoys the code to remote servers,
returns False if unsuccessful
"""
from fabric.api import *  # 'pragmaticsm over best practice'
from os.path import exists
pack = __import__('1-pack_web_static')
deploy = __import__('2-do_deploy_web_static')

env.hosts = ['54.157.166.142', '18.209.178.215']
env.user = "ubuntu"


def deploy():
    """
    Deploy a webpage to remote servers

    Args:
    None

    Return:
    True if it succesful calls all imported functions and ran successfully,
    otherwise, False
    """
    archive_path = pack.do_pack()
    if not exists(archive):
        return False
    else:
        status = deploy.do_deploy(archive_path)
        return status
