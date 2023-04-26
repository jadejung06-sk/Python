import os
from os.path import isdir, join
from threading import Lock, Thread

mutex = Lock()
matches = []

def file_search(root, filename):
    print("Searching in:", root)
    child_threads = []
    for file in os.listdir(root):
        full_path = join(root, file)
        if filename in file:
            mutex.acquire()
            matches.append(full_path)
            mutex.release()
        if isdir(full_path):
            t = Thread(target= file_search, args = ([full_path, filename]))
            t.start()
            child_threads.append(t) 
    for t in child_threads:
        # print('t :', t) # <Thread(Thread-3945 (file_search), stopped 8104)>
        t.join()
            # print('1', isdir(full_path)) # True, False
            # file_search(full_path, filename)
            
def main():
    t = Thread(target= file_search, args = (["C:\Program Files", "README.md"]))
    # file_search("C:\Program Files", "README.md")
    t.start()
    t.join()
    for m in matches:
        print("Matched:", m)
        
main()

'''
Matched: C:\Program Files\MariaDB 10.3\README.md
Matched: C:\Program Files\Git\mingw64\share\doc\git-lfs\README.md
Matched: C:\Program Files\WindowsPowerShell\Modules\Pester\3.4.0\README.md
Matched: C:\Program Files\Git\mingw64\doc\git-credential-manager-core\README.md
Matched: C:\Program Files\Microsoft Visual Studio\2022\Community\Common7\IDE\Extensions\Microsoft\LiveShare\Agent\SOS_README.md
Matched: C:\Program Files\Microsoft Visual Studio\2022\Community\Msbuild\Microsoft\VisualStudio\NodeJs\node_modules\npm\node_modules\libnpmpublish\README.md
Matched: C:\Program Files\Microsoft Visual Studio\2022\Community\Msbuild\Microsoft\VisualStudio\NodeJs\node_modules\npm\node_modules\libnpmteam\README.md
Matched: C:\Program Files\Microsoft Visual Studio\2022\Community\Msbuild\Microsoft\VisualStudio\NodeJs\node_modules\npm\node_modules\node-gyp\gyp\README.md
Matched: C:\Program Files\Microsoft Visual Studio\2022\Community\Msbuild\Microsoft\VisualStudio\NodeJs\node_modules\npm\node_modules\which\README.md
'''