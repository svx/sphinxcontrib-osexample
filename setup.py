# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

long_desc = '''
This package contains the osexample Sphinx extension.

This extension adds support for Operating systems code block
widget to Sphinx.
'''

requires = ['Sphinx>=1.0']

setup(
    name='sphinxcontrib-osexample',
    version='0.1.1.dev0',
    url='https://github.com/svx/sphinxcontrib-osexample',
    download_url='http://pypi.python.org/pypi/sphinxcontrib-osexample',
    license='BSD',
    author='Sven Strack',
    author_email='sven@so36.net',
    description='Sphinx extension for OS code-blocks',
    keywords = "Sphinx extension",
    long_description=long_desc,
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
	'Programming Language :: Python :: 2.7',
        'Topic :: Documentation',
        'Topic :: Utilities',
    ],
    platforms='any',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requires,
    namespace_packages=['sphinxcontrib'],
)
