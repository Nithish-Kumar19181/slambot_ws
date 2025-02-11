from setuptools import find_packages
from setuptools import setup

setup(
    name='slambot_controller',
    version='0.0.0',
    packages=find_packages(
        include=('slambot_controller', 'slambot_controller.*')),
)
