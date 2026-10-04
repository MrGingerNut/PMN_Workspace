#############################################################
# p04-philos_manners.py
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
from threading import Semaphore, Thread, Event

EATING   = 0
HUNGRY  = 1
THINKING = 2

CRAVING = 0 # new hunger levels
HUNGRY2 = 1
UNCONMFORTABLY_HUNGRY = 2
VERY_HUNGRY = 3
STARVING = 4
names = ['CRAVING', 'HUNGRY2', 'UNCOMFORTABLY_HUNGRY', 'VERY_HUNGRY', 'STARVING']

states = []
hunger_states = []
philosophers = []   # Threads
forks = []          # Forks
mutex = Semaphore(1)
stop = Event() # for when a philosopher is starving

def left(p):
    return (p + len(philosophers)-1) % len(philosophers)
#end def

def right(p):
    return (p + 1) % len(philosophers)
#end def

def take_fork(p, f):
    print(f'Philosopher {p} tries to take fork {f}')
    if not forks[f].acquire(timeout=1):
        return False
    print(f'Philosopher {p} takes fork {f}')
    return True
#end def

def put_fork(p, f):
    forks[f].release()
    print(f'Philosopher {p} puts fork {f} down')
#end def

def think(p):
    states[p] = THINKING
    print(f'Philosopher {p} is thinking')
    sleep(0.001 * randint(500, 1500))
    states[p] = HUNGRY
    hunger_states[p] = CRAVING
    print(f'Philosopher {p} is now {names[hunger_states[p]]}')
#end def

def eat(p):
    print(f'Philosopher {p} is eating')
    states[p] = EATING
    sleep(0.001 * randint(500, 1500))
#end def

def philosopher(p):
    left_fork, right_fork = p, right(p)
    if p == len(philosophers) - 1:  # the last philosopher takes right fork first
        left_fork, right_fork = right_fork, left_fork # pal otro lado
    # stop is an event so is initially flase
    while not stop.is_set(): # return true if and only if the internal flag is true
        ate = False # to know if a philosopher ate or not
        #Initially philosophers are hungry. They eat.
        if take_fork(p, left_fork):          # take left fork
            try:
                if take_fork(p, right_fork):   # tries to take right fork
                    try:
                        eat(p) # tries to eat
                        ate = True
                    finally:
                        # After eating philosophers release forks...
                        put_fork(p, right_fork)
            finally:
                put_fork(p, left_fork) # if doesnt grab right fork release left fork
        if ate:
            #...and think
            think(p)
        else:
            hunger_states[p] = hunger_states[p] + 1
            print(f'Philosopher {p} is now {names[hunger_states[p]]}')
            if hunger_states[p] == STARVING:
                print(f'Philosohper {p} starved to death. Poor philosopher {p}')
                stop.set() # Set the internal flag to true. All threads waiting for it to become true are awakened.
#end def

def main(args):
    n = 5
    global states, philosophers, hunger_states
    if len(args) > 1 and ord(args[1]) > 5:
        n = ord(args[1]) 

    for i in range(n):
        states.append(HUNGRY)  # Philosophers are initially hungry
        forks.append(Semaphore(1)) # creates free fork
        philosophers.append(Thread(target=philosopher, args=[i]))
        hunger_states.append(CRAVING) # first hunger staet
    for i in range(n):
        philosophers[i].start()  # Philosopher lives!
    sleep(60)
#end def

if __name__ == '__main__':
    main(sys.argv)