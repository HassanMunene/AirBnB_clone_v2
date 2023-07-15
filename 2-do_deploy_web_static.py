#!/usr/bin/python3
"""
compress the web static package
"""
from invoke import task
from fabric.api import *
from datetime import datetime
from os import path

env.hosts = ['3.90.85.212', '52.203.214.248']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/id_rsa'

@task
def do_deploy(archive_path):
    """
    deploy the compressed archive to the
    two web servers
    """
    try:
        if not (path.exists(archive_path)):
            return False
        put(archive_path, '/tmp/')
        timestamp = archive_path[-18:-4]
        run('sudo mkdir -p /data/web_static/releases/web_static_{}'.format(timestamp))
        run('sudo tar -xzf /tmp//web_static_{}.tgz -C /data/web_static/releases/web_static_{}/'.format(timestamp, timestamp))

        # delete the archive after uncompressing
        run ('sudo rm /tmp/web_static_{}.tgz'.format(timestamp))

        # move the contents into host web_static
        run('sudo mv /data/web_static/releases/web_static_{}/web_static/* /data/web_static/releases/web_static_{}'.format(timestamp, timestamp))

        run('sudo rm -rf /data/web_static/releases/web_static_{}/web_static'.format(timestamp))

        # delete pre-exisiting sym link
        run('sudo rm -rf /data/web_static/current')

        # create the symlink again
        run('sudo ln -s /data/web_static/releases/web_static_{}/ /data/web_static/current'.format(timestamp))
    except:
        return False

    return True
