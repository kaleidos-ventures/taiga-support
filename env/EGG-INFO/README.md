# pygments-markdown-lexer

A [Markdown](https://daringfireball.net/projects/markdown/syntax) lexer
for [Pygments](http://pygments.org/) to highlight Markdown code snippets.

 [![Travis CI](https://api.travis-ci.org/jhermann/pygments-markdown-lexer.svg)](https://travis-ci.org/jhermann/pygments-markdown-lexer)
 [![Coveralls](https://img.shields.io/coveralls/jhermann/pygments-markdown-lexer.svg)](https://coveralls.io/r/jhermann/pygments-markdown-lexer)
 [![GitHub Issues](https://img.shields.io/github/issues/jhermann/pygments-markdown-lexer.svg)](https://github.com/jhermann/pygments-markdown-lexer/issues)
 [![License](https://img.shields.io/pypi/l/pygments-markdown-lexer.svg)](https://github.com/jhermann/pygments-markdown-lexer/blob/master/LICENSE)
 [![Development Status](https://img.shields.io/pypi/status/pygments-markdown-lexer.svg)](https://pypi.python.org/pypi/pygments-markdown-lexer/)
 [![Latest Version](https://img.shields.io/pypi/v/pygments-markdown-lexer.svg)](https://pypi.python.org/pypi/pygments-markdown-lexer/)


## Installation

*Pygments Markdown Lexer* can be installed via ``pip install pygments-markdown-lexer`` as usual,
see [releases](https://github.com/jhermann/pygments-markdown-lexer/releases) for an overview of available versions.
To get a bleeding-edge version from source, use these commands:

```sh
repo="jhermann/pygments-markdown-lexer"
pip install -r "https://raw.githubusercontent.com/$repo/master/requirements.txt"
pip install -UI -e "git+https://github.com/$repo.git#egg=${repo#*/}"
```

See [Contributing](#contributing) on how to create a full development environment.


## Usage

Once installed, usually into a virtualenv, the ``pygments_markdown_lexer`` package
is instantly visible to *Pygments*, since it defines a *Setuptools* entry point
for registration.

In order for *Sphinx* to load and recognize the custom lexer, add the
``pygments_markdown_lexer`` package name to the ``extensions`` list in ``conf.py``.
Then use it in a ``code-block`` as if it were a built-in, like this:

    .. code-block:: md

        Enables _Pygments_ to handle
        [Markdown](https://daringfireball.net/projects/markdown/syntax)
        in *Sphinx* **code blocks**.

Both ``md`` and ``markdown`` are valid to specify the language for the code block.


## Contributing

To create a working directory for this project, call these commands:

```sh
git clone "https://github.com/jhermann/pygments-markdown-lexer.git"
cd "pygments-markdown-lexer"
. .env --yes --develop
invoke build --docs test check
```

Contributing to this project is easy, and reporting an issue or
adding to the documentation also improves things for every user.
You don’t need to be a developer to contribute.
See [CONTRIBUTING](https://github.com/jhermann/pygments-markdown-lexer/blob/master/CONTRIBUTING.md) for more.


## References

**Specs**

* [Markdown Syntax](https://daringfireball.net/projects/markdown/syntax#p)
* [Pygments Lexer](http://pygments.org/docs/lexerdevelopment/)
* [Pygments Tokens](http://pygments.org/docs/tokens/)
* [Pygments Styles](http://pygments.org/docs/styles/)
  * [Style Gallery](https://help.farbox.com/pygments.html)
* [Python Regex](https://docs.python.org/2/library/re.html)

**Tools**

* [Sphinx](http://sphinx-doc.org/)
* [Pygments](http://pygments.org/)
* [Cookiecutter](http://cookiecutter.readthedocs.io/en/latest/)
* [PyInvoke](http://www.pyinvoke.org/)
* [pytest](http://pytest.org/latest/contents.html)
* [tox](https://tox.readthedocs.io/en/latest/)
* [Pylint](http://docs.pylint.org/)
* [twine](https://github.com/pypa/twine#twine)
* [bpython](http://docs.bpython-interpreter.org/)
* [yolk3k](https://github.com/myint/yolk#yolk)

**Packages**

* [Rituals](https://jhermann.github.io/rituals)


## Acknowledgements

* Based in part on the ``pygments.lexers.markup`` lexers (*Georg Brandl* and others, BSD-licensed).
