#! /usr/bin/env python3
"""Install script."""

from setuptools import setup


setup(
    name="adac",
    use_scm_version={"local_scheme": "node-and-timestamp"},
    setup_requires=["setuptools_scm"],
    author="HOMEINFO - Digitale Informationssysteme GmbH",
    author_email="<info at homeinfo dot de>",
    maintainer="Richard Neumann",
    maintainer_email="<r dot neumann at homeinfo priod de>",
    install_requires=["requests"],
    py_modules=["adac"],
    entry_points={"console_scripts": ["adaclt = adac:main"]},
    description="ADAC traffic news API client.",
)
