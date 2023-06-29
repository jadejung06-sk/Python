##### install git
### > https://git-scm.com/download/win
'''
use visual Studio Code as git's default editor
override the default branch name for new repositiories : main
'''

##### git config : user and email
### any folder > right click on the mouse > powershell
'''
git config --global user.email "jjs@naver.com"
git config --global user.name "jjs"
'''

##### git init
### working folder > new terminal
'''
git init
#####
git add app.txt          [git add file name]
git add .
#####
git commit -m "new file"
git status
git log --all --oneline
'''