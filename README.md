# Taiga-support [![Build Status](https://travis-ci.org/taigaio/taiga-support.svg?branch=master)](https://travis-ci.org/taigaio/taiga-support)

User suport pages for Taiga. See https://support.taiga.io.


## For Developers

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


#### Commands

```lektor server -f webpack```
: Run the dev server.

```lektor build -f webpack```
: Build the web site.

```lektor deploy ghpages```
: [CI Enabled] Deploy in [GitHub pages](http://taigaio.github.io/taiga-support/).

```lektor clean```
: Cleans the entire build folder.
