from setuptools import setup, find_packages

setup(
    name='libPairGenerator',
    version='0.0.1a', 
    url='https://github.com/asparks1987/libpairgenerator',
    author='Aryn M. Sparks',
    author_email='Aryn.sparks1987@gmail.com',
    description='Script for generating data sets of XOR values.',
    packages=find_packages(),    
    install_requires=['pytz'],
)