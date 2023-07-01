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
## merge when a code in the same position is modified
'''
## multiprocessing
git switch main
git merge multiprocessing
## delete manualy the code
git add .
git commit -m "merged"
'''
## merge when a code in the different position is modified
'''
## multiprocessing
git switch main
git merge multiprocessing
git add .
git commit -m "merged"
'''
## jump and merge
'''
git merge -squash multiprocessing
git add .
git commit -m "merged"
'''

############################################################

##### delete branch because branch keeps forever
## after merging
'''
git branch -d multiprocessing
''' 
## before merging
'''
git branch -D multiprocessing
'''

###########################################################

##### modify commits and make a new commit
'''
git restore [filename]
git resotre --source [commitID]
'''
##### modify contents
'''
git revert [commitID] [coomitID] [...]
git revert HEAD
'''

###########################################################

##### Remote git 
## change master branch to main branch
'''
git branch -M main
git push -u [https://~.git] [branchname]
git push -u https://.git main
'''
##### set variable
'''
git remote add [variable_nm] [https://~.git]
git remote add origin https://~.git
git remote -v
git push -u origin main #branchname
## after -u oring main
git push
'''

##### collaboration
'''
git clone https://~.git
git pull https://~.git
git push
'''
##### new remote branch
'''
git branch mining
git switch mining
git add .
git commit -m "remote branch"
git push origin mining
## online github > pull request == merge > create pull request > squash
'''