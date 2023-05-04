##### Basic github
## >>> https://github.com/cutajarj/multithreadinginpython

##### github directory download
## >>>https://webnautes.tistory.com/1387
## copy github address
'''
https://github.com/cutajarj/multithreadinginpython.git
'''
## copy directory without repository
'''
/metarfiles/
'''
## commend on the terminal 
'''
cd parallel_compute
cd multiprocess
mkdir metarfiles
cd metarfiles
git init
git config core.sparsecheckout True
git remote add -f origin https://github.com/cutajarj/multithreadinginpython.git
echo metarfiles/* > .git/info/sparse-checkout
git pull origin master
'''