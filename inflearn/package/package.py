"""
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
  -> jadejung
  -> type password
  -> verity email and two factor authentication (2FA)
 
7. Modify something ver. 1.0.0 to ver. 1.0.1
 -> setup.py version 1.0.1
 -> build : dir -> cd <path of setup.py> -> python setup.py sdist bdist_wheel
 -> delete files version 1.0.0
 -> python -m twine upload dist/* 

"""

from jpgTogif.jpytogif import GifConverter as gfc

import os

print(os.getcwd())

## create Class
c = gfc( './inflearn/package/jpgTogif/images/*.png', './inflearn/package/jpgTogif/output/result.gif', (320, 240))
c.convert_gif()
