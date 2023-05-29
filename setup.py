from setuptools import setup, find_packages
import os

with open("README.md", "r") as fh:
    long_description = fh.read()

from src.util import (
    get_version,
)

packages = find_packages()
# the directories where the code is
# so knows it should be included
package_data = {"src": ["src/*"]}

# for pypi
data_files = [(".", ["LICENCE", "README.md"])]


CLASSIFIERS = [
    "Environment :: Console",
    "Environment :: MacOS X",
    "Intended Audience :: Science/Research",
    "License :: OSI Approved :: MIT license",
    "Natural Language :: English",
    "Operating System :: POSIX :: Linux",
    "Operating System :: MacOS :: MacOS X",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
    "Topic :: Scientific/Engineering :: Bio-Informatics",
]



setup(
    name="dnaapler",
    version=get_version(),
    zip_safe=True,
    author="George Bouras",
    description="Re-orients assembled sequences",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author_email="george.bouras@adelaide.edu.au",
    packages=find_packages(),
    package_data=package_data,
    data_files=data_files,
    include_package_data=True,
    scripts=["dnaapler"],
    url="https://github.com/gbouras13/dnaapler",
    python_requires=">=3.7",
    classifiers=CLASSIFIERS,
    install_requires=[
        "pyyaml>=6.0",
        "pytest-runner >= 5.0.0",
        "biopython >=1.76",
        "pytest>=6.2.5",
        "pandas>=1.4.2",
        "loguru>=0.5.3",
        "Click>=8.0.0",
        "pytest-cov>=3.0.0",
        "pyrodigal>=2.0.0",
    ],
)

