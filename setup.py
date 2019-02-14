#!/usr/bin/env python
from setuptools import setup

setup(
    name="tap-googlesheets",
    version="0.1.0",
    description="Singer.io tap for extracting data",
    author="Indicium.tech",
    url="https://Indicium.tech",
    classifiers=["Programming Language :: Python :: 3 :: Only"],
    py_modules=["tap_googlesheets"],
    install_requires=[
        "singer-python>=5.0.12",
        "requests",
        "google-api-python-client==1.7.8",
        "google-auth==1.6.2",
        "google-auth-httplib2==0.0.3",
        "google-auth-oauthlib==0.2.0",
        "httplib2==0.12.0",
        "uritemplate==3.0.0",
        "oauth2client==3.0.0"
    ],
    entry_points="""
    [console_scripts]
    tap-googlesheets=tap_googlesheets:main
    """,
    packages=["tap_googlesheets"],
    package_data={
        "schemas": ["tap_googlesheets/schemas/*.json"]
    },
    include_package_data=True,
)
