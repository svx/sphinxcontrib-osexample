.. sphinxcontrib-osexample documentation master file, created by
   sphinx-quickstart on Wed Dec 23 16:49:36 2015.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

sphinxcontrib-osexample
=======================

.. toctree::
   :maxdepth: 2

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

Currently supported are: Debian, Ubuntu, Fedora, CentOS, OSX

Quick Example
-------------

Source would look something like this::

    .. example-code::
        .. code-block:: Debian

            sudo apt install htop

        .. code-block:: Fedora

            sudo dnf install htop

        .. code-block:: OSX

            brew install htop


This will create an output like this:

.. image:: https://raw.githubusercontent.com/svx/sphinxcontrib-osexample/master/docs/_static/example.gif
   :alt: Example how it looks like as generated HTML


Installation
------------

.. code-block:: bash

    $ pip install sphinxcontrib-osexample


Enabling the extension in Sphinx
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Just add sphinxcontrib.examplecode to the list of extensions in the conf.py file. For example:

.. code-block:: bash

    extensions = ['sphinxcontrib.osexample']



