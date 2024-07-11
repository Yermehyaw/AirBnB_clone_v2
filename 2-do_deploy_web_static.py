#!/usr/bin/python3
# Use this fab file only after compressing web_static/ using the
# do_path() function in 0-setup_web_static.sh

"""
Modules Imported: fabric.api

fabric.api: Abstraction of the original fabric. Used for remote and local code
deployment and sys admin tasks. Streamlines the use of SSH
"""
from fabric.api import *  # "pargmatism over best practices" :)


def do_deploy(archive_path):
    """"
    Distributes an archive to web servers. Kindly change the server
    addresses/IP in the env.hosts object to the one of your desired server

    Attributes:
    archive_path(str): Path to archived web content for transfer

    Return:
    True, if all operations are completed successfully, otherwise, False
    """
    archive_name =  # use regex to retrieve only archive name without .tgz extension
    if [ ]:  # Checks if file dosent exists at archive_path
        return False
    env.hosts = ["54.157.166.142", ""]  # Server's IP addresses
    env.user = "ubuntu"
    # Use a with statement to encapsulate all this commands to a remote server?
    sudo(f"mv {archive_path} /tmp/")  # is a recursive mv needed and does sudo delete at remote or local?
    run(f"tar --uncompress {archive_path} /data/web_static/releases/{archive_name}")  # the command to uncompress .tgz files is?
    sudo(f"rm -r {archive_path}")  # delete archive from server
    sudo(f"rm /data/web_static/current")
    run("ln -s /data/web_static/releases/{archive_name}")
    
    end = local("echo $?", capture=True)  # Check the exit status after running
    if end.stdout == 0:
        return True
    else:
        return False
