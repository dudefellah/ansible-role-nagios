[![pipeline status](https://gitlab.com/dudefellah/ansible-role-nagios/badges/main/pipeline.svg)](https://gitlab.com/dudefellah/ansible-role-nagios/-/commits/main)

nagios
=========

This role is responsible for installing and configuring
[Nagios Core](https://www.nagios.org/projects/nagios-core/). In addition to
nagios-core, the role will also install
[Nagios Plugins](https://www.nagios.org/downloads/nagios-plugins/) in order to
make your nagios install useful. Some relevant documentation exists in
[defaults/main.yml](defaults/main.yml) related to the sources and installation
options for both Nagios Core and Nagios Plugins.

Once installed, Nagios configuration can be set by declaring a list of nagios
configurations to be installed through any combination of YAML, local files
and/or local directories.

Requirements
------------

There are probably implications for your Python version in the template
provided for custom nagios configs generated in YAML through this role. If
you are making use of this feature, you should probably avoid using Python 2
as your Python interpreter when using this role.

Role Variables
--------------

All variables are described in [defaults/main.yml](defaults/main.yml).

Dependencies
------------

None.

Example Playbook
----------------

    - hosts: nagios_servers
      roles:
         - include_role: perdu.nagios
           vars:
             nagios_configs:
               - dest: objects/contacts-test.cfg
                 config:
                   contact:
                     contact_name: somebody
                     use: generic-contact
                     alias: Just Some Person
                     email: me@myhost

License
-------

GPLv2+

Authors Information
------------------

- Dan - github.com/dudefellah
- Célestin Matte - github.com/Perdu
