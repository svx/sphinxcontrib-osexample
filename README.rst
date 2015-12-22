.. -*- restructuredtext -*-

:author: Sven Strack <sven@so36.net>

==============================
osexample extension for Sphinx
==============================

This is a modified fork of Serge Domkowski's `examplecode extension <https://bitbucket.org/birkenfeld/sphinx-contrib/src/7f39b7f255e34bfe588f0065a5d9709a7d8e7614/examplecode/?at=default>`_ for Sphinx.

About
=====

This is a simple extension that, when rendered as HTML, will fold multiple
code blocks containing different operating systems administration examples into a single block
which can be toggled from one to another using buttons.

It's intended to be used for displaying package manager examples.
(e.g., apt install or dnf install).

This extension adds the ``example-code`` directive which adds a class to
a container wrapping the code blocks that should be folded. The class allows
the included Javascript and CSS to render the folded block and buttons.

Quick Example
-------------

Source would look something like this::

    .. example-code::
        .. code-block:: Debian

            sudo apt install htop

        .. code-block:: Fedora

            sudo dnf install htop

Installation
------------

t.b.c

Documentation
-------------

Full documentation for end users can be found in the "docs" folder.

Contribute
----------

- Issue Tracker: github.com/svx/sphinxcontrib-osexample/issues
- Source Code: github.com/svx/sphinxcontrib-osexample

Support
-------

If you are having issues, please let us know.


License
-------

The project is licensed under BSD.