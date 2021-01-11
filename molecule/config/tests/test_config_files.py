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
    nagios_procs = host.process.filter(user="nagios", comm="nagios")
    assert (nagios_procs is not None) and (len(nagios_procs) > 0)

    assert host.file("/usr/local/etc/nagios/test_nagios.cfg").exists
    assert host.file("/usr/local/etc/nagios/test/commands.cfg").exists
    assert host.file("/usr/local/etc/nagios/test1/commands.cfg").exists
    assert host.file("/usr/local/etc/nagios/test2/commands.cfg").exists
    assert host.file("/usr/local/etc/nagios/test3/commands.cfg").exists
    assert host.file("/usr/local/etc/nagios/test4/commands.cfg").exists
    assert host.file("/usr/local/etc/nagios2/test5/commands.cfg").exists


    assert host.file("/usr/local/etc/nagios/nagios.cfg").contains(
                "cfg_file=/usr/local/etc/nagios/test/commands.cfg"
                )
    assert host.file("/usr/local/etc/nagios/nagios.cfg").contains(
                "cfg_file=/usr/local/etc/nagios/test1/commands.cfg"
                )
    assert host.file("/usr/local/etc/nagios/nagios.cfg").contains(
                "cfg_file=/usr/local/etc/nagios/test2/commands.cfg"
                )
    assert host.file("/usr/local/etc/nagios/nagios.cfg").contains(
                "cfg_file=/usr/local/etc/nagios/test3/commands.cfg"
                )
    assert host.file("/usr/local/etc/nagios/nagios.cfg").contains(
                "cfg_file=/usr/local/etc/nagios/test4/commands.cfg"
                )
    assert host.file("/usr/local/etc/nagios/nagios.cfg").contains(
                "cfg_file=/usr/local/etc/nagios2/test5/commands.cfg"
                )
