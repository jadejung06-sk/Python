from threading import Lock, Thread

from deadlocks_train.hierachy.train import *
from deadlocks_train.draw_trains import *
from deadlocks_train.model import *

train_length = 200

def main():
    win = GraphWin('Trains in a box', 800, 800) 
    win.setBackground('black')
    train_anim = TrainAnim(win, train_length)
    
    while True:
        train_anim.update_trains(trains, intersections)
        time.sleep(0.01)
        
main()