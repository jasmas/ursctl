ursctrl
#######

ursctrl is a Cisco Umbrella Roaming Security module for AnyConnect control utility.
It can be used to disable, enable or check the current status of the module.

Installation
------------

Install ursctrl using the latest version of setuptools and pip::

    $ python3 -m pip install --upgrade setuptools pip
    $ python3 -m pip install ursctrl

Usage
-----

Execute using the module directly or using the convenience script::

    $ python3 -m ursctl
    Cisco Umbrella Roaming Security module for AnyConnect control utility
    usage: ursctl [option]::
     	-d, --disable	Disable the module
     	-e, --enable	Enable the module
     	-s, --status	Print module status

    $ ursctl
    Cisco Umbrella Roaming Security module for AnyConnect control utility
    usage: ursctl [option]::
        -d, --disable   Disable the module
        -e, --enable    Enable the module
        -s, --status    Print module status

