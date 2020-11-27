import sys

from filehandler import read_csv

from state import State
from aialgorithms import alpha_star,best_fs

people = read_csv(sys.argv[1])
limit = int(sys.argv[2])

initial_state = State(people)
terminal_state = alpha_star(initial_state, limit)

if terminal_state is not None:
    if terminal_state.get_score() > limit:
        print("Solution not found, due to exceeded time limit.")
    else:
        print("The family crossed the bridge in " + str(terminal_state.get_score()) + " seconds.")
        temp = terminal_state
        path = [terminal_state]
        while temp.get_father() is not None:
            path.append(temp.get_father())
            temp = temp.get_father()
        [x.print() for x in path[::-1]]


