"""
RDS-HOST
=======

A simple command line utility, allowing you to find the hostname associated with
your Amazon RDS instance name.

Also has a wrapper for PostgreSQL's psql utility. If you are using MySQL or Oracle,
patches are welcome.

A few examples:

::
TODO FIXME
    % ec2-ssh nginx2
    # equivalent to
    # ssh ubuntu@ec2-123-45-67-89.compute-1.amazonaws.com

    % ec2-ssh root@appserver
    % ec2-ssh deploy@nginx2 sudo restart nginx

    # accompanying ec2-host script

    # w/o arg: prints all active instances
    % ec2-host
    django1 ec2-123-45-67-89.compute-1.amazonaws.com
    django2 ec2-132-45-67-89.compute-1.amazonaws.com
    django3 ec2-231-45-67-89.compute-1.amazonaws.com

    # w/ arg: prints host name of matching instance
    % ec2-host django2
    django2 ec2-132-45-67-89.compute-1.amazonaws.com


Changelog
`````````

* 0.0.1 - playing around; forked from ec2-ssh 1.2.1
"""


import os
from setuptools import setup


setup(
    name = "rds-host",
    version = "0.0.1",
    author = "Neil Kandalgaonkar",
    author_email = "neilk@neilk.net",
    description = "Get hostname from Amazon RDS instance name",
    long_description = __doc__,
    license = "MIT",
    url = "https://github.com/Instagram/ec2-ssh",
    keywords = ["amazon", "aws", "ec2", "ami", "ssh", "cloud", "boto", "rds"],
    install_requires = ['boto>=1.0'],
    scripts = ["bin/rds-host", "bin/rds-psql"],
    classifiers = [
        "Programming Language :: Python",
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Utilities"
        ],
)
