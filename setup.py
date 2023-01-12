# -*- coding: utf-8 -*-

import sys
from setuptools import setup

if sys.version_info[0] < 3:
    with open("README.md", "r") as fh:
        long_description = fh.read()
else:
    with open("README.md", "r", encoding="utf-8") as fh:
        long_description = fh.read()

setup(
    name="turn_alerts",
    version="1.0.0",
    description="Client library for use with the Turn notifications microservice",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Amir Canto",
    author_email="amir@turn.ai",
    packages=["turn_alerts", "turn_alerts.schemas"],
    install_requires=["marshmallow>=3.19.0", "requests>=2.28.1"],
    tests_require=["nose>=1.3.7"],
    test_suite="nose.collector",
)
