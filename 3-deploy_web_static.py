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
#pack = __import__('1-pack_web_static')
#deploy = __import__('2-do_deploy_web_static')

env.hosts = ['54.157.166.142', '18.209.178.215']
env.user = "ubuntu"
env.key_filename = '~/.ssh/id_rsa'


def deploy():
    """
    A function in this fabfile used to deploy a webpage to remote servers

    Args:
    None

    Return:
    The return value of another executed fabfile
    """
    archive_path = local("fab -f 1-pack_web_static.py do_pack", capture=True)
    if not exists(archive_path):
        return False
    else:
        status = local("fab -f 2-do_deploy_web_static.py\
 do_deploy:archive_path={archive_path}", capture=True)
        return status
