# -*- coding: utf-8 -*-
# pylint: disable=bad-whitespace
# flake8: noqa
"""
    Pygments Markdown Lexer – A Markdown lexer for Pygments to
    highlight Markdown code snippets.

    Copyright ©  2015 Jürgen Hermann <jh@web.de>

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""
from __future__ import absolute_import, unicode_literals, print_function

from .lexer import MarkdownLexer

__url__             = "https://github.com/jhermann/pygments-markdown-lexer"
__version__         = "0.2.0"
__license__         = "Apache 2.0"
__author__          = "Jürgen Hermann"
__author_email__    = "jh@web.de"
__keywords__        = "hosted.by.github pygments markdown lexer highlighting"


def setup(app):
    """ Initializer for Sphinx extension API.

        See http://www.sphinx-doc.org/en/stable/extdev/index.html#dev-extensions.
    """
    lexer = MarkdownLexer()
    for alias in lexer.aliases:
        app.add_lexer(alias, lexer)

    return dict(version=__version__)


__all__ = ['MarkdownLexer', 'setup']
