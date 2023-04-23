import json
import urllib.request
import time
from threading import Thread

finished_counter = 0


def counter_letter(url, frequency):
    response = urllib.request.urlopen(url)
    txt = str(response.read())
    for l in txt:
        letter = l.lower()
        if letter in frequency:
            frequency[letter] += 1
    global finished_counter
    finished_counter += 1
            
def main():
    frequency = {}
    for c in "abcdefghijklmnopqrstuvwxyz":
        frequency[c] = 0
    start = time.time()
    for i in range(1000, 1020):
        Thread(target = counter_letter, args= (f"https://www.rfc-editor.org/rfc/rfc{i}.txt", frequency)).start()
        # counter_letter(f"https://www.rfc-editor.org/rfc/rfc{i}.txt", frequency)
    # print(finished_counter)
    while finished_counter < 20:
        time.sleep(0.5)
    end = time.time()
    print(json.dumps(frequency, indent = 4))
    print("Done, time taken", end - start)

main()


'''
    "d": 40501, 
    "e": 140093,
Not exact but quicker (Due to Race condition, quite rare)

Need syncronization 
'''