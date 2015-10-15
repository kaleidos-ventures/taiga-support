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

- Install Nikola
```
mkvirtualenv -p /usr/bin/python3 taiga-support
pip install -r requirements.txt
```


### Commands

- ```nikola auto -b```  
  Start a dev server
- ```nikola github_deploy```  
  Deploy in github pages
- ```nikola help```  
  Show help information about nikola
