
from setuptools import setup, find_packages

setup(
    name='licensechain-sdk',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
    author='LicenseChain',
    description='Python SDK for LicenseChain to validate licenses using LicenseChain APIs.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/LicenseChain/LicenseChain-Python-SDK',
    license='Elastic 2.0',
)
