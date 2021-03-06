#!/usr/bin/env python

from setuptools import setup

setup(
    name='mockldap-fork',
    version='0.1.6',
    description=u"Mockldap fork, A simple mock implementation of python-ldap.",
    long_description=open('README').read(),
    url='http://bitbucket.org/psagers/mockldap/',
    author='Peter Sagerson',
    author_email='psagers.pypi@ignorare.net',
    license='BSD',
    packages=['mockldap'],
    package_dir={'': 'src/'},
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Web Environment',
        'Programming Language :: Python',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: BSD License',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: System :: Systems Administration :: Authentication/Directory :: LDAP',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    keywords=['mock', 'ldap'],
    install_requires=[
        'python-ldap',
    ],
    extras_require={
        'passlib': ['passlib>=1.6.1'],
        'mock': ['mock'],
    },
    setup_requires=[
        'setuptools>=0.6c11',
    ],
    test_suite='mockldap.tests',
)
