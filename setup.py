#!/usr/bin/env python3
from distutils.core import setup
setup(
    name='wemo',
    packages=['wemo'],
    version='1.1.0',
    description='A Wemo API',
    author='Evan Elias Young',
    url='https://github.com/evaneliasyoung/wemo',
    download_url='https://github.com/evaneliasyoung/wemo/archive/master.tar.gz',
    keywords=['wemo', 'api', 'automation'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Home Automation',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3.7'
    ],
    install_requires=[
        'requests',
        'pytest'
    ],
    python_requires='~=3.7'
)
