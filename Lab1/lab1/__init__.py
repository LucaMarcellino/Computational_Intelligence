import random
from tkinter.tix import INTEGER
import numpy as np
from typing import Callable
from gx_utils import *
import logging
import itertools

def problem(N, seed=None):
    random.seed(seed)
    return [
        list(set(random.randint(0, N - 1) for n in range(random.randint(N // 5, N // 2))))
        for n in range(random.randint(N, N * 5))
    ]
def InitialState(list_):
    all_lists = sorted(problem(N, seed=42), key=lambda l: len(l))
    return all_lists[0]




class State:
    def __init__(self, data: np.ndarray):
        self._data = data.copy()
        self._data.flags.writeable = False

    def __hash__(self):
        return hash(bytes(self._data))

    def __eq__(self, other):
        return bytes(self._data) == bytes(other._data)

    def __lt__(self, other):
        return bytes(self._data) < bytes(other._data)

    def __str__(self):
        return str(self._data)

    def __repr__(self):
        return repr(self._data)

    '''
    def data.tolist(self):
        list_tot = list()
        list_tot.append(self._data.all())
        return list_tot
    '''

    @property
    def data(self):
        return self._data

    def copy_data(self):
        return self._data.copy()

def priority_function(state: State):
     list_ = state.data.tolist()
     return sum(len(s) for s in list_)

def possible_actions(all_list: list, actualState):
    all_list1 = all_list.copy()
    val = actualState[-1]
    while val in all_list1:
        all_list1.remove(val)
    return all_list1 
    
def goal_test(state,N):
    print(state, type(state))
    set_ = set()
    for el in state:
            set_.add(el)

    #set_ = set(list(itertools.chain.from_iterable(state)))
    print(set_)
    set_2 = set(range(N))
    print(set_2)
    return set_ == set_2


def result(state, a):
    state.append(a)
    return State(np.array(state, dtype=object))

def search(
    all_list,
    initial_state: State,
    goal_test: Callable,
    parent_state: dict,
    state_cost: dict,
    priority_function: Callable,
    unit_cost: Callable,
    number : INTEGER
):
    frontier = PriorityQueue()
    parent_state.clear()
    state_cost.clear()

    state = State(np.array(initial_state.data.tolist()))
    parent_state[state] = None
    state_cost[state] = len(state.data.tolist())
    solution = []

    while state is not None and not goal_test(state.data.tolist(),N):
        for a in possible_actions(all_list[0:],state.data.tolist()):
            new_state = result(state.data.tolist(), a)
            cost = unit_cost(a)
            if new_state not in state_cost and new_state not in frontier:
                parent_state[new_state] = state
                state_cost[new_state] = state_cost[state] + cost
                frontier.push(new_state, p=priority_function(new_state))
                logging.debug(f"Added new node to frontier (cost={state_cost[new_state]})")
            elif new_state in frontier and state_cost[new_state] > state_cost[state] + cost:
                old_cost = state_cost[new_state]
                parent_state[new_state] = state
                state_cost[new_state] = state_cost[state] + cost
                logging.debug(f"Updated node cost in frontier: {old_cost} -> {state_cost[new_state]}")
        if frontier:
            state = frontier.pop()
        else:
            state = None

    path = list()
    path = list()
    s = state
    i = 50

    logging.info(f"Found a solution in {len(path):,} steps; visited {len(state_cost):,} states")
    print(f"Initial blocks : {all_list}")
    print(f"Solution: {state}")
    print(f"Parent State Dict: {parent_state}")
    print(f"Path: {list(reversed(path))}")
    return list(reversed(path))            

parent_state = dict()
state_cost = dict()
for N in [5]:
    GOAL = set(range(N))
    INITIAL_STATE = State(np.array(InitialState(problem(N))))
    all_lists = sorted(problem(N, seed=42), key=lambda l: len(l))
    search(
        all_lists,
        initial_state = INITIAL_STATE,
        goal_test=goal_test,
        parent_state=parent_state,
        state_cost=state_cost,
        priority_function= priority_function,
        unit_cost= lambda a: len(a),
        number= N
        )
    
