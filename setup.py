import os
from setuptools import setup, find_packages

path = os.path.abspath(__file__)

try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
except(IOError, ImportError):
    long_description = open(os.path.join(path, 'README.md')).read()

data_files = []
for dirpath, dirnames, filenames in os.walk(path):
    for i, dirname in enumerate(dirnames):
        if dirname.startswith('.'):
            del dirnames[i]
    if '__init__.py' in filenames:
        continue
    elif filenames:
        data_files.append([dirpath, [os.path.join(dirpath, f) for f in filenames]])

with open(os.path.join(path, "requirements.txt")) as requirements_file:
    requirements = requirements_file.readlines()

setup(
    name="geryon-fs",
    version="0.1",
    author="Diego J. Romero López",
    author_email="diegojromerolopez@gmail.com",
    description=" fuse-based driver for Mongo databases written in Python.",
    long_description=long_description,
    classifiers=[
        'Programming Language :: Python :: 3.9'
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: BSD License'
    ],
    install_requires=requirements,
    license="BSD 2-clause",
    keywords="database mongo fuse driver",
    url='https://github.com/diegojromerolopez/geryon-fs',
    packages=find_packages(path),
    data_files=data_files,
    include_package_data=True,
)