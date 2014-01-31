"""
RDS-HOST
========

A simple command line utility, allowing you to find the hostname associated with
your Amazon RDS instance name.

Also has a simple wrapper for PostgreSQL's psql utility. If you want a similar
script for MySQL or Oracle, patches are welcome.

A few examples:

::
    # w/o arg: prints all active instances
    % rds-host
    mydbinstance    mydbinstance.c6ulnjwxjm.us-west-2.rds.amazonaws.com:5432
    myotherdbinstance  myotherdbinstance.d5ulnswdjyf.us-west-2.rds.amazonaws.com:5432

    # w/ arg: prints host name of matching instance
    % rds-host mydbinstance
    mydbinstance.c6ulnjwxjm.us-west-2.rds.amazonaws.com:5432

    # connect to the instance with psql
    % rds-psql mydbinstance -U mydbuser mydbname
    psql>


Changelog
`````````

* 0.1.0 - more or less works
* 0.0.1 - playing around; forked from ec2-ssh 1.2.1
"""

from setuptools import setup


setup(
    name = "rds-host",
    version = "0.1.0",
    author = "Neil Kandalgaonkar",
    author_email = "neilk@neilk.net",
    description = "Get hostname from Amazon RDS instance name",
    long_description = __doc__,
    license = "MIT",
    url = "https://github.com/Instagram/ec2-ssh",
    keywords = ["amazon", "aws", "ec2", "ami", "ssh", "cloud", "boto", "rds"],
    install_requires = ['boto>=2.2'],
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
