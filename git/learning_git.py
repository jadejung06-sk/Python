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
git log --all --oneline    [q : quit]
'''

##### git difference
# > extension : git graph
'''
git difftool 558c482c3 [commit id]
git config --global diff.tool vscode
git config --global difftool.vscode.cmd 'code --wait --diff $LOCAL $REMOTE'
'''

##### before working a copy
'''
git branch multiprocessing
git switch multiprocessing
git status
git add .
git commit -m "multiprocessing"
git log --all --oneline --graph
'''
### merge when a code in the same position is modified

### merge when a code in the different position is modified