# Taiga-support [![Build Status](https://travis-ci.org/taigaio/taiga-support.svg?branch=master)](https://travis-ci.org/taigaio/taiga-support)

User suport pages for Taiga.


## For Developers

You need:

 - python 2.7
 - node >= 5.0
 - ruby


#### Setup

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
#### Envs

- [Test Env - GitHub Pages](http://taigaio.github.io/taiga-support/)

#### Commands

```lektor server -f webpack```
: Run the dev server.

```lektor build -f webpack```
: Build the web site.

```lektor deploy ghpages```
: [CI Enabled] Deploy in GitHub Pages.

```lektor clean```
: Cleans the entire build folder.
