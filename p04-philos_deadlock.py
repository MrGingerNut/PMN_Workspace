#############################################################
# p04-philos_deadlock.py
#
# Author: Felix Garcia Santiago
#
# Dijkstra's dining philosophers prolem
#
# ##
#############################################################
import sys
from time import sleep
from random import randint, uniform
from threading import Semaphore, Thread

EATING   = 0
HUNGRY   = 1
THINKING = 2

states = []
philosophers = []   # Threads
forks = []          # Forks
mutex = Semaphore(1)

def left(p):
    return (p + len(philosophers)-1) % len(philosophers)
#end def

def right(p):
    return (p + 1) % len(philosophers)
#end def

def take_fork(p, f):
    print(f'Philosopher {p} tries to take fork {f}')
    forks[f].acquire() 
    print(f'Philosopher {p} takes fork {f}')
#end def

def put_fork(p, f):
    forks[f].release()
    print(f'Philosopher {p} puts fork {f} down')
#end def

def think(p):
    states[p] = THINKING
    print(f'Philosopher {p} is thinking')
    sleep(0.001 * randint(500, 1500))
    print(f'Philosopher {p} is now hungry')
    states[p] = HUNGRY
#end def

def eat(p):
    print(f'Philosopher {p} is eating')
    states[p] = EATING
    sleep(0.001 * randint(500, 1500))
#end def

def philosopher(p):
    left_fork, right_fork = p, right(p)
    if p == len(philosophers) - 1:  # the last philosopher takes right fork first
        left_fork, right_fork = right_fork, left_fork 
    while(True):
        #Initially philosophers are hungry. They eat.
        take_fork(p, left_fork)          # take left fork
        try:
            take_fork(p, right_fork)   # tries to take right fork
            try:
                eat(p) # tries to eat
            finally:
                # After eating philosophers release forks...
                put_fork(p, right_fork)
        finally:
            put_fork(p, left_fork) # if doesnt grab right fork release left fork
        #...and think
        think(p)
#end def

def main(args):
    n = 5
    global states, philosophers
    if len(args) > 1 and int(args[1]) > 5:
        n = int(args[1]) # ord returns an unicode >:(

    for i in range(n):
        states.append(HUNGRY)  # Philosophers are initially hungry
        forks.append(Semaphore(1)) # creates free fork
        philosophers.append(Thread(target=philosopher, args=[i]))
    for i in range(n):
        philosophers[i].start()  # Philosopher lives!
    sleep(15)
#end def

if __name__ == '__main__':
    main(sys.argv)