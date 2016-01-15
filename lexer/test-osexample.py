# -*- coding: utf-8 -*-
import re
from pygments.lexer import RegexLexer, bygroups
from pygments.token import Keyword, Number, Text, Comment

__all__ = ['UbuntuLexer', 'CentosLexer', 'FedoraLexer']

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
class CentosLexer(RegexLexer):
    name = 'Centos'
    aliases = ['centos']
    filenames = ['*.ubuntu']

    tokens = {
        'root': [
        (r'\byum\b', Keyword),
        (r'\b((yum)?update\b)', Keyword),
        (r'\b((yum)?install\b)', Keyword),
        (r'\b((yum-)?check\b)', Keyword),
        (r'\s', Text),
        (r'-', Text),
        (r'\S+', Keyword.Pseudo),
        (r'[;#].*', Comment.Single),
        ],
    }

class FedoraLexer(RegexLexer):
    name = 'Fedora'
    aliases = ['fedora']
    filenames = ['*.ubuntu']

    tokens = {
        'root': [
        (r'\bdnf\b', Keyword),
        (r'\b((dnf)?update\b)', Keyword),
        (r'\b((dnf)?install\b)', Keyword),
        (r'\b((dnf-)?check\b)', Keyword),
        (r'\s', Text),
        (r'-', Text),
        (r'\S+', Keyword.Pseudo),
        (r'[;#].*', Comment.Single),
        ],
    }