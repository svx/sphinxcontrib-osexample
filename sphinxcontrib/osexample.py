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
from sphinx.highlighting import lexers
from pygments.lexer import RegexLexer, bygroups
from pygments.lexers import get_lexer_by_name
from pygments.token import Literal, Text, Operator, Keyword, Name, Number
from pygments.util import ClassNotFound



CSS_FILE = 'osexample.css'
JS_FILE = 'osexample.js'

class UbuntuLexer(RegexLexer):
    """
    Lexer for Ubuntu
    """

    name = 'Ubuntu'
    aliases = ['ubuntu']

    EXTRA_KEYWORDS = set(('apt', 'apt-get'))

    def get_tokens_unprocessed(self, text):
        for index, token, value in PythonLexer.get_tokens_unprocessed(self, text):
            if token is Name and value in self.EXTRA_KEYWORDS:
                yield index, Keyword.Pseudo, value
            else:
                yield index, token, value

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
    try:
        get_lexer_by_name('ubuntu')
    except ClassNotFound:
        app.add_lexer('ubuntu', UbuntuLexer())
    app.connect('builder-inited', add_assets)
    app.connect('build-finished', copy_assets)

