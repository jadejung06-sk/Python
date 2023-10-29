# pygifconvt

## Table of Contents
  * [Installation](#installation)
  * [Quick start](#quick-start)
  * [Features](#features)
  
## Installation

Download using pip via pypi.

```bash
$ pip install 'imagestogif_js' --upgrade
  or
$ pip install git+'https://github.com/jadejung06-sk/Python.git'
```
(Mac/homebrew users may need to use ``pip3``)


## Quick start
```python
 >>> from imagestogif_js.converter import GifConverter
 >>> c = GifConverter("your original images path", 'your gif output path', (320,240))
 >>> c.convert_gif()
```

## Features
  * Python library to convert single oder multiple frame gif images
  * OpenCV does not support gif images.