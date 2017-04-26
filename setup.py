from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name = 'i3-config-builder',
    version = '0.1',
    description = 'Command Line i3 config builder',
    long_description = long_description,
    author = 'Brian LeBlanc',
    author_email = 'brileb73@gmail.com',
    url = 'https://github.com/brileb73/i3-config-builder',
    license = 'MIT',
    packages = find_packages(exclude = ['contrib', 'docs', 'tests']),
    install_requires = ['argparse'],
    extras_require = {
        ':python_version=="2.6"': [
            'argparse>=1.1'
        ]
    },
    entry_points = {
        'console_scripts': [
            'i3cfgbuild=i3cfgbuild.main:main'
        ]
    }
)

