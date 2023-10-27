"""
PyPI, build, package deploy
    
"""

from jpgTogif.jpytogif import GifConverter as gfc

import os

print(os.getcwd())

## create Class
c = gfc( './inflearn/package/jpgTogif/images/*.png', './inflearn/package/jpgTogif/output/result.gif', (320, 240))
c.convert_gif()
