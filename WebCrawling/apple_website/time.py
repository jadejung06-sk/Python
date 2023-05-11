import time

print(time.time()) # Epoch/Unix Time
print(time.ctime(time.time()))

current_time = time.localtime()
current_time = time.strftime('%Y year %m month %d day', current_time)
print(current_time)

import datetime
simple_date = datetime.datetime(2023, 5, 12, 6, 15, 30)
print(simple_date)
