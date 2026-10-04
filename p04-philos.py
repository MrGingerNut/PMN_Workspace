#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ##
#############################################################
# philosophers.py
#
# Author: Mauricio Matamoros
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
    forks[p].acquire() 
    print(f'Philosopher {p} takes fork {f}')
#end def

def put_fork(p, f):
    forks[p].release()
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
    while(True):
        #Initially philosophers are hungry. They eat.
        take_fork(p, p)          # Left fork
        take_fork(p, right(p))   # Right fork
        eat(p)
        # After eating philosophers release forks...
        put_fork(p, p)
        put_fork(p, right(p))
        #...and think
        think(p)
#end def

def main(args):
    n = 5
    global states, philosophers
    if len(args) > 1 and ord(args[1]) > 5:
        n = ord(args[1])

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