"""
######## PyPI 
PyPI, build, package deploy
1. PyPI - Register (ID == Username) jadejung
2. check the structure of the project
3. write __init__.py
4. write some files like LICENSE, setup.py, MANIFEST.in, README.md, requirements.txt, setup.cfg
5. pip install setuptools, wheel to make a setup file
  -> method 1 : python -m pip install --upgrade setuptools wheel
  -> method 2 : python -m pip install --user --upgrade setuptools wheel
  -> build : dir -> cd <path of setup.py> -> python setup.py sdist bdist_wheel
  
6. Check *.tar, *.whl in dist folder
  - PypI deploy :
  <path of setup.py>
  -> pip install twine 
  -> python -m twine upload dist/*
  -> jadejungg
  -> type password
  -> verity email and two factor authentication (2FA)
 
7. Modify something ver. 1.0.0 to ver. 1.0.1
 -> setup.py version 1.0.1
 -> build : dir -> cd <path of setup.py> -> python setup.py sdist bdist_wheel
 -> delete files version 1.0.0
 -> python -m twine upload dist/* 

8. Install my package
 -> pip install imagestogif_js
 from imagestogif_js.converter import GifConverter as gfc
"""

"""
######## Github 
Github, package deploy
0. pip uninstall imagestogif_js -> pip list
1. https://github.com - Resgister + extension 
 -> git config --global user.anem
 -> git config --global user.email
 -> git config credential.helper store
 -> git config --list
2. check installed git
3. git add -> commit -> push
 -> git repository
 -> git init
 -> git add .
 -> git status
 -> git commit -m "message"
 -> git remote add origin "your repository http"
 -> git push origin master
4. git push PyPI package in your repostory
5. pip install git+https://your-repository-url



"""


from jpgTogif_forPyPI.jpytogif import GifConverter as gfc

import os

print(os.getcwd())

## create Class
c = gfc( './inflearn/package/jpgTogif/images/*.png', './inflearn/package/jpgTogif/output/result.gif', (320, 240))
c.convert_gif()
