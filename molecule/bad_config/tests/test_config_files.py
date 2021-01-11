import json

import os

import re

import sys

import testinfra.utils.ansible_runner

import uuid

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_config_files(host):
    host.run("systemctl stop nagios")
    host.run("systemctl start nagios")

    assert host.service("nagios").is_running

    # Make sure that our bad config file isn't the one present
    assert not host.file("/usr/local/etc/nagios/nagios.cfg").contains(
                "# Whoops, I forgot to add all of these files!"
                )
