"""
PyPI, build, package deploy
1. PyPI - Register (ID == Username) jadejung
2. 

"""

from jpgTogif.jpytogif import GifConverter as gfc

import os

print(os.getcwd())

## create Class
c = gfc( './inflearn/package/jpgTogif/images/*.png', './inflearn/package/jpgTogif/output/result.gif', (320, 240))
c.convert_gif()
