#/usr/bin/env python
import os
import sys
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.md')).read()

version = __import__('king').__version__

setup(
    name='django-king',
    version=version,
    description='Utilities for Django projects',
    long_description=README,
    author='Thiago Faria de Andrade',
    author_email='thiagofa@gmail.com',
    maintainer='Thiago Faria de Andrade',
    maintainer_email='thiagofa@gmail.com',
    license='New BSD License',
    url='https://github.com/thiagofa/django-king',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
    ],
)