# Taiga-support

![Kaleidos Project](http://kaleidos.net/static/img/badge.png "Kaleidos Project")
[![Managed with Taiga.io](https://taiga.io/media/support/attachments/article-22/banner-gh.png)](https://taiga.io "Managed with Taiga.io")
[![Build Status](https://travis-ci.org/taigaio/taiga-support.svg?branch=master)](https://travis-ci.org/taigaio/taiga-support)

User suport pages for Taiga.


#### Envs

- **Stable** (Production Env): [https://tree.taiga.io/support/](https://tree.taiga.io/support/)
- **Dev** (Test Env): [https://taigaio.github.io/taiga-support/](https://taigaio.github.io/taiga-support/)


#### Setup

You need:

 - python 2.7
 - node >= 5.0
 - ruby
 - virtualenvwraper


- Install Lektor
```
mkvirtualenv -p /usr/bin/python2.7 taiga-support
pip install -r requirements.txt
```

- SASS (need ruby)
```
gem install sass
export PATH=":$PATH:$(ruby -e "print Gem.user_dir")/bin"
sass -v             # should return something like 'Sass 3.4.11 (Selective Steve)'
```

- Install Webpack
```
cd taiga-support/webpack
npm install
```


#### Commands

```lektor server -f webpack```
: Run the dev server.

```lektor build -f webpack```
: Build the web site.

```lektor deploy ghpages```
: [CI Enabled] Deploy in GitHub Pages.

```lektor clean```
: Cleans the entire build folder.


#### Code of Conduct

Help us keep the Taiga Community open and inclusive. Please read and follow our [Code of Conduct](https://github.com/taigaio/code-of-conduct/blob/master/CODE_OF_CONDUCT.md).
