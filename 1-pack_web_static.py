#!/usr/bin/python3
from invoke import run as local
from invoke import task
from datetime import datetime


@task
def do_pack(context):
    """
    creates a .tgz archiver from contents of webstatic
    we will also create a folder called versions that will contain
    the archive files
    """
    now = datetime.now()
    timestamp = now.strftime("%Y%m%d%H%M%S")
    archive_name = "web_static_{}.tgz".format(timestamp)
    archive_path = "versions/{}".format(archive_name)

    local("mkdir -p versions")
    local("tar -czvf {} web_static".format(archive_path))

    return archive_path
