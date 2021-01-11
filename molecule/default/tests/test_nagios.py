import json

import os

import re

import sys

import testinfra.utils.ansible_runner

import uuid

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_backup_files(host):

    if host.ansible.get_variables()['inventory_hostname'] not in [
            'nagios-molecule-debian-stretch-instance',
            'nagios-molecule-debian-buster-instance']:
        assert host.service("nagios").is_running

    if (
            host.ansible.get_variables()['inventory_hostname'].endswith('centos-7-instance')
    ):
        assert host.file("/usr/local/etc/nagios/test/commands.cfg").exists
        assert host.file("/usr/local/etc/nagios/nagios.cfg").contains(
                "cfg_file=/usr/local/etc/nagios/test/commands.cfg"
                )
