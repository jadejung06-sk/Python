import re
import time
from multiprocessing import Queue, Process
# (45, 11),(41,45),(36,20)

PTS_REGEX = "\((\d*),(\d*)\)"
TOTAL_PROCESS = 8

def find_area(points_queue):
    points_str = points_queue.get()
    while points_str is not None:
        points = []
        area = 0.0
        for xy in re.finditer(PTS_REGEX, points_str):
            # print('xy', xy)
            # print(xy.group(1), xy.group(2)) # 16 73
            points.append((int(xy.group(1)), int(xy.group(2))))
    # xy <re.Match object; span=(1611, 1618), match='(151,1)'>
        for i in range(len(points)):
            a, b = points[i], points[(i + 1) % len(points)]
            area += a[0] * b[1] - a[1] * b[0]
    # a (148, 4)
    # b (146, 4)      
        area += abs(area) / 2.0
        points_str = points_queue.get()
        # print(area)


if __name__ == "__main__":
    queue = Queue(maxsize=1000)
    processes = []
    for i in range(TOTAL_PROCESS):
        p = Process(target = find_area, args = (queue,)) # TypeError
        processes.append(p)
        p.start()
    f = open('./parallel_compute/multiprocess/polygons.txt')
    # print('f.read()', f.read()) # 내용 전체를 문자열로 리턴
    lines = f.read().splitlines()
    start = time.time()
    for line in lines:
        queue.put(line) # <multiprocessing.queues.Queue object at 0x0000020A55E5BFD0>
        # print(queue)
        # find_area(line)
    for _ in range(TOTAL_PROCESS): queue.put(None)
    for p in processes: p.join()
    end = time.time()
    print("Time taken", end - start)
    # Time taken 6.4921441078186035  vs. Time taken 2.2295024394989014
    
    
    
    ##### txt.splitlines()
    # >>> https://homzzang.com/b/py-197
    '''
    txt = "홈짱닷컴\nHomzzang.com"
    x = txt.splitlines(True)
    print(x)
    >>> ['홈짱닷컴\n', 'Homzzang.com']
    '''