import os
from setuptools import setup

root_dir_path = os.path.dirname(os.path.abspath(__file__))

long_description = open(os.path.join(root_dir_path, "README.md")).read()

requirements_path = os.path.join(root_dir_path, "requirements.txt")
with open(requirements_path) as requirements_file:
    requirements = requirements_file.readlines()

setup(
    name="geryon-fuse",
    version="0.1",
    author="Diego J. Romero López",
    author_email="diegojromerolopez@gmail.com",
    description=" fuse-based driver for Mongo databases written in Python.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: BSD License"
    ],
    install_requires=requirements,
    license="BSD 2-clause",
    keywords="database mongo fuse driver",
    url="https://github.com/diegojromerolopez/geryon-fuse",
    packages=["mongofs", "logger"],
    package_dir={"mongofs": "src/mongofs", "logger": "src/logger"},
    data_files=[("resources", ["resources/.geryonfuse.ini"])],
    include_package_data=True,
    scripts=[
        "bin/create_empty_config.py",
        "bin/mount_mongofs.py"
    ]
)
