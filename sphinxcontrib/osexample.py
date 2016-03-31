# -*- coding: utf-8 -*-
"""
Examplecode specs
=================
"""
import os
import re
from docutils.parsers.rst import Directive
from docutils import nodes
from sphinx.util.osutil import copyfile
from pygments.lexers import get_lexer_by_name
from pygments.lexer import RegexLexer, bygroups


CSS_FILE = 'osexample.css'
JS_FILE = 'osexample.js'

__all__ = ['UbuntuLexer', 'CentosLexer', 'FedoraLexer', 'OSXLexer']

class UbuntuLexer(RegexLexer):
    name = 'Ubuntu'
    aliases = ['ubuntu', 'debian', 'Debian']
    filenames = ['*.ubuntu']


class CentosLexer(RegexLexer):
    name = 'Centos'
    aliases = ['centos', 'CentOS']


class FedoraLexer(RegexLexer):
    name = 'Fedora'
    aliases = ['fedora']


class OSXLexer(RegexLexer):
    name = 'OSX'
    aliases = ['osx']
   

class ExampleCodeDirective(Directive):
    """
    This directive is intended to be used to contain a group of
    code blocks which are beingused to show OS examples for Ubuntu, Debian,
    Fedora, CentOS and OSX.
    When rendered as HTML the the examples will all be rolled up
    into a single display area with buttons to select between the different
    languages.
    """

    has_content = True

    def run(self):
        self.assert_has_content()
        text = '\n'.join(self.content)
        node = nodes.container(text)
        node['classes'].append('example-code')
        self.add_name(node)
        self.state.nested_parse(self.content, self.content_offset, node)
        return [node]


def add_assets(app):
    app.add_stylesheet(CSS_FILE)
    app.add_javascript(JS_FILE)

def copy_assets(app, exception):
    if app.builder.name != 'html' or exception:
        return
    app.info('Copying osexample stylesheet/javascript... ', nonl=True)
    dest = os.path.join(app.builder.outdir, '_static', CSS_FILE)
    source = os.path.join(os.path.abspath(os.path.dirname(__file__)), CSS_FILE)
    copyfile(source, dest)
    dest = os.path.join(app.builder.outdir, '_static', JS_FILE)
    source = os.path.join(os.path.abspath(os.path.dirname(__file__)), JS_FILE)
    copyfile(source, dest)
    app.info('done')

def setup(app):
    app.add_directive('example-code',  ExampleCodeDirective)
    app.connect('builder-inited', add_assets)
    app.connect('build-finished', copy_assets)
    try:
	get_lexer_by_name('ubuntu')
	get_lexer_by_name('fedora')
	get_lexer_by_name('centos')
    except ClassNotFound:
	app.add_lexer('Ubuntu', UbuntuLexer())
	app.add_lexer('Debian', UbuntuLexer())
	app.add_lexer('Fedora', FedoraLexer())
	app.add_lexer('CentOS', CentosLexer())
    app.add_lexer('OSX', OSXLexer())