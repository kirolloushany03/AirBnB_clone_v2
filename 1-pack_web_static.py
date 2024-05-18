#!/usr/bin/python3
""" a Fabric script that generates a .tgz archive from
the contents of the web_static folder"""

from datetime import datetime
from fabric.api import local


def do_pack():
    """generates a .tgz archive """

    dt = datetime.utcnow()
    file = "versions/web_static_{}{}{}{}{}{}.tgz".format(
        dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second)

    result = local("mkdir -p versions")
    if result.failed:
        return None

    # create a compressed archive file in the .tgz format
    result = local("tar -czf {} web_static".format(file))
    if result.failed:
        return None

    return file
