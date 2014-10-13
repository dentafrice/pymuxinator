import os
from setuptools import setup

setup(
    name = "pymuxinator",
    version = "0.0.1",
    author = "Caleb Mingle",
    author_email = "caleb@mingle.cm",
    description = "Python version of Tmuxinator",
    url = "http://caleb.io",
    packages=["pymuxinator", "tests"],
    tests_require=[
        "nose>=1.0",
        "mock>=1.0",
    ],
    install_requires=[
        "pyyaml>=1.0",
        "Jinja2>=1.0",
    ],
    test_suite = "nose.collector"
)
