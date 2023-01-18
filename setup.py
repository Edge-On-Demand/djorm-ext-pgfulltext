from setuptools import find_packages
from setuptools import setup


setup(
    packages=find_packages(),
    version='0.9.4',
    pbr=True,
    setup_requires=['pbr'],
)
