#!/usr/bin/python3
# Use this fab file only after compressing web_static/ using the
# do_path() function in 0-setup_web_static.sh

"""
Modules Imported: fabric.api, os.path

fabric.api: Abstraction of the original fabric. Used for remote and local code
deployment and sys admin tasks. Streamlines the use of SSH

os.path: Execute shell path commands. The exixts(), basename() and splitext()
methods are the methods of interest.
"""
from os.path import exists
from os.path import basename
from os.path import splitext
from fabric.api import *  # "pragmatism over best practices" :)


def do_deploy(archive_path):
    """"
    Distributes an archive to web servers. Kindly change the server
    addresses/IP in the env.hosts object to the one of your desired server

    Attributes:
    archive_path(str): Path to archived web content for transfer

    Return:
    True, if all operations are completed successfully, otherwise, False
    """
    if exists(archive_path):  # Checks if file dosent exists at archive_path
        return False
    # Retrieve only archive name without .tgz extension
    name_with_ext = basename(archive_path)  #remove path 
    archive_name = splitext(name_with_ext)[0]  # remove file extension from file name
    env.hosts = ["54.157.166.142", "18.209.178.215"]  # IP to exec commands in
    env.user = "ubuntu"  # default user, if none is entered via fab -u

    # Fabric commands
    sudo("mkdir -p /tmp/")  # create target dir if it dosent exist
    put(f"mv -f {archive_path} /tmp/")  # works without sudo.
    sudo(f"mkdir -p /data/web_static/releases/{archive_name}/")
    sudo(f"tar -xzf /tmp/{archive_path} /data/web_static/releases/{archive_name}/")
    sudo(f"rm -rf /tmp/{archive_name}/")   # delete archive from server
    sudo(f"rm -f /data/web_static/current")  # delete previous sum link at  /current
    sudo(f"touch /data/web_static/current")  # recreate /current file for sym link
    sudo("ln -sf /data/web_static/releases/{archive_name}/ /data/web_static/current")  # link archive folder to /current file

    end = local("echo $?", capture=True)  # Check the exit status after running
    if end.stdout == 0:
        return True
    else:
        return False
