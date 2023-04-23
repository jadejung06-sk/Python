import json
import urllib.request
import time
from threading import Thread, Lock

finished_counter = 0


def counter_letter(url, frequency, mutex):
    response = urllib.request.urlopen(url)
    txt = str(response.read())
    mutex.acquire()
    for l in txt:
        letter = l.lower()
        if letter in frequency:
            frequency[letter] += 1
    global finished_counter
    finished_counter += 1
    mutex.release()
            
def main():
    frequency = {}
    mutex = Lock()
    for c in "abcdefghijklmnopqrstuvwxyz":
        frequency[c] = 0
    start = time.time()
    for i in range(1000, 1020):
        Thread(target = counter_letter, args= (f"https://www.rfc-editor.org/rfc/rfc{i}.txt", frequency, mutex)).start()
        # counter_letter(f"https://www.rfc-editor.org/rfc/rfc{i}.txt", frequency)
    # print(finished_counter)
    ##### w/o mutex
    # while finished_counter < 20:
        # time.sleep(0.5)
    ##### with mutex
    while True:
        mutex.acquire()
        if finished_counter == 20:
            break
        mutex.release()
        time.sleep(0.5)
    end = time.time()
    print(json.dumps(frequency, indent = 4))
    print("Done, time taken", end - start)

main()


'''
### 1
    "d": 40501, 
    "e": 140093,
Not exact but quicker (Due to Race condition, quite rare)
Need syncronization 
### 2
using mutex
Done, time taken 1.79 s vs. 16.1 s (single thread)
'''