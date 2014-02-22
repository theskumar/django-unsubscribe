#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

setup(
    name='django-unsubscribe',
    version='0.1.0',
    description='Easily send one-click un-subscribable newletter type emails from \
                django to keep your customers happy.',
    long_description=readme + '\n\n' + history,
    author='Saurabh Kumar',
    author_email='thes.kumar@gmail.com',
    url='https://github.com/theskumar/django-unsubscribe',
    packages=[
        'unsubscribe',
    ],
    package_dir={'unsubscribe': 'unsubscribe'},
    include_package_data=True,
    install_requires=[
        'Django >= 1.4.3',
    ],
    zip_safe=False,
    classifiers=[
            'Development Status :: 2 - Pre-Alpha',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: BSD License',
            'Programming Language :: Python :: 2.6',
            'Programming Language :: Python :: 2.7',
            'Environment :: Web Environment',
            'Framework :: Django',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: BSD License',
            'Operating System :: OS Independent',
            'Programming Language :: Python',
            'Programming Language :: Python :: 2',
            'Programming Language :: Python :: 3',
            'Topic :: Utilities'
        ],
)
