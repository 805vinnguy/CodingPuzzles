# To Climb N Stairs
# Author: Vinh Nguyen

def count_ways(N, X):
    count = 0
    start = Node(0, N)
    frontier = [start]
    while(len(frontier) > 0):
        state = frontier.pop()
        #print(str(state.value) + " : " + str(state.steps_remaining))
        if(state.steps_remaining == 0):
            count += 1
            continue
        if(state.steps_remaining < 0):
            continue
        for step_choice in X:
            #if(state.steps_remaining % step_choice == 0):
            next_state = Node(state.value + step_choice, N)
            frontier.append(next_state)
    return count

class Node:

    def __init__(self, value, N):
        self.value = value
        self.steps_remaining = N - value
