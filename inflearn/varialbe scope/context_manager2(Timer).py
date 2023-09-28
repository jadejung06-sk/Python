"""
Measure execution (Timer)
"""

##### Ex 1
# Use class

import time

class ExcuteTimer(object):
    
    def __init__(self, msg):
        self._msg = msg
        
    def __enter__(self):
        self._start = time.monotonic()
        return self._start
        
    def __exit__(self, exc_type, exc_value, exc_traceback):
        if exc_type:
            print("Logging exception {}".format((exc_type, exc_value, exc_traceback)))
        else:
            print("{} : {:.3f} s".format(self._msg, time.monotonic() - self._start))
        return True
    
with ExcuteTimer('Processing Time : ') as v:
    # print('Received start monotonic1 : {}'.format(v))
    for i in range(1000000):
        pass
    raise Exception('Raise! Exception!') ## 강제 발생
## Processing Time :  : 0.016 s