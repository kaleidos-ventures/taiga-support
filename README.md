# Taiga-support

User suport pages for Taiga.

See https://support.taiga.io.


## For Developers

#### Setup

- SASS (need ruby)
```
gem install sass scss-lint
export PATH=":$PATH:$(ruby -e "print Gem.user_dir")/bin"
sass -v             # should return something like 'Sass 3.4.11 (Selective Steve)'
```

- Install Lektor
```
mkvirtualenv -p /usr/bin/python2.7 taiga-support
pip install -r requirements.txt
```


### Commands

- ````command``  
  description
