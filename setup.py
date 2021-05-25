import os
from setuptools import setup

root_dir_path = os.path.dirname(os.path.abspath(__file__))

try:
    import pypandoc
    long_description = pypandoc.convert("README.md", "rst")
except(IOError, ImportError):
    long_description = open(os.path.join(root_dir_path, "README.md")).read()

with open(os.path.join(root_dir_path, "requirements.txt")) as requirements_file:
    requirements = requirements_file.readlines()

setup(
    name="geryon-fuse",
    version="0.1",
    author="Diego J. Romero López",
    author_email="diegojromerolopez@gmail.com",
    description=" fuse-based driver for Mongo databases written in Python.",
    long_description=long_description,
    classifiers=[
        "Programming Language :: Python :: 3.9"
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: BSD License"
    ],
    install_requires=requirements,
    license="BSD 2-clause",
    keywords="database mongo fuse driver",
    url="https://github.com/diegojromerolopez/geryon-fuse",
    packages=["mongofs"],
    package_dir={"mongofs": "src/mongofs"},
    data_files=[("resources", ["resources/.geryonfuse.ini"])],
    include_package_data=True,
    scripts=[
        "bin/create_empty_config.py",
        "bin/mount_mongofs.py"
    ]
)
