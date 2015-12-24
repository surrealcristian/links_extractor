#!/usr/bin/env python3

import os
import sys


try:
    from setuptools import setup
except:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist bdist_wheel upload')
    sys.exit()

setup(
    name='links_extractor',
    version='0.0.1',
    description='Extract links from a URL',
    author='Cristian Cabrera',
    author_email='surrealcristian@gmail.com',
    url='https://github.com/surrealcristian/links_extractor',
    keywords='links extractor url',
    install_requires=['requests>=2', 'lxml>=3'],
    license='MIT',
    py_modules=['links_extractor'],
    scripts=['links_extractor.py'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Software Development :: Libraries',
        'Topic :: Utilities',
        'Topic :: Internet :: WWW/HTTP',
    ],
)
