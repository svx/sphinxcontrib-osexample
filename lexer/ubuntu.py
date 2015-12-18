# -*- coding: utf-8 -*-
import re
from pygments.lexer import RegexLexer, bygroups
from pygments.token import Keyword, Number, Text, Comment

__all__ = ['UbuntuLexer']

class UbuntuLexer(RegexLexer):
    name = 'Ubuntu'
    aliases = ['ubuntu']
    filenames = ['*.ubuntu']

    tokens = {
	    'root': [
		(r'\bapt\b', Keyword),
		(r'\b((apt-)?get\b)', Keyword),
		(r'\s', Text),
		(r'-', Text),
		(r'\S+', Keyword.Pseudo),
		(r'[;#].*', Comment.Single),
	    ],
    }
