.. -*- restructuredtext -*-

.. image:: https://readthedocs.org/projects/sphinxcontrib-osexample/badge/?version=stable
    :target: http://sphinxcontrib-osexample.readthedocs.org/en/latest/?badge=stable
    :alt: Documentation Status


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


This will create an output like this:

.. image:: https://raw.githubusercontent.com/svx/sphinxcontrib-osexample/master/docs/_static/example.gif
   :alt: Example how it looks like as generated HTML


Installation
------------

.. code-block:: bash

    $ sphinxcontrib-osexample


Enabling the extension in Sphinx
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Just add sphinxcontrib.examplecode to the list of extensions in the conf.py file. For example:

.. code-block:: bash

    extensions = ['sphinxcontrib.osexample']



Documentation
-------------

Full documentation for end users can be found in the "docs" folder.

It is also available online on `Read The Docs <https://sphinxcontrib-osexample.readthedocs.org/en/latest/>`_

Contribute
----------

- `Issue Tracker <https://github.com/svx/sphinxcontrib-osexample/issues>`_
- `Source Code <https://github.com/svx/sphinxcontrib-osexample>`_

Support
-------

If you are having issues, please let us know.


License
-------

The project is licensed under BSD.
