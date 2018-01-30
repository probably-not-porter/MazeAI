#### AI Lab A
#### CS365 : Artificial Intelligence
# Porter Libby

import math
import random
import time

#Data structure to represent an instance of the environment
class State_instance():
    def __init__(self,grid,cost,x,y,goals_ls):
        self.path_cost = cost     #environment variables
        self.grid = grid
        self.player_xy = [x,y]
        self.goals = goals_ls

def transition_function(action,state):      #take an action and a state and return an action
    new_state = State_instance(state.grid,(state.path_cost)+1,state.player_xy[0],state.player_xy[1],state.goals)

    if action == 'n':
        new_state.player_xy[0] += -1
        new_state.grid[state.player_xy[0]][state.player_xy[1]] = '#'
    elif action == 's':
        new_state.player_xy[0] += 1
        new_state.grid[state.player_xy[0]][state.player_xy[1]] = '#'
    elif action == 'w':
        new_state.player_xy[1] += -1
        new_state.grid[state.player_xy[0]][state.player_xy[1]] = '#'
    elif action == 'e':
        new_state.player_xy[1] += 1
        new_state.grid[state.player_xy[0]][state.player_xy[1]] = '#'

    new_state.goals = count_goals(new_state.grid)
    return new_state

def print_grid(grid):   #print a grid so that it can be viewed
    for x in range(len(grid)):
        line = ""
        for y in range(len(grid[x])):
            line += grid[x][y]
        print(line)

def parse_file(url):    #convert txt file into grid system of nested lists
    lines = [line.rstrip('\n') for line in open(url)] #split by line
    grid = []

    for x in lines:     #splice each line by the character
        line = []

        for y in range(len(x)):
            line.append(x[y])
        grid.append(line)

    return grid     #return completed structure

def player_start(grid):     #find the x,y coordinates of the player at init
    print('finding player...')
    for x in range(len(grid)):  #iterate over layers

        for y in range(len(grid[x])):     #iterate over elements of layers
            if grid[x][y] == "P":   #if player start is found
                return [x,y]

    return None

def count_goals(grid):      #find the x,y coordinates of all goals on the map.
    goals = []
    for x in range(len(grid)):  #iterate over layers

        for y in range(len(grid[x])):     #iterate over elements of layers
            if grid[x][y] == ".":   #if a goal is found
                goals.append([x,y])     # add to goal list

    return goals

def get_actions(state):     #get all the actions possible from a given state
    grid = state.grid
    px = state.player_xy[0]
    py = state.player_xy[1]
    actions_ls = []

    if grid[px - 1][py] == ' ':
        actions_ls.append('n')
    if grid[px][py - 1] == ' ':
        actions_ls.append('w')
    if px < len(grid):
        if grid[px + 1][py] == ' ':
            actions_ls.append('s')
    if py < len(grid[0]):
        if grid[px][py + 1] == ' ':
            actions_ls.append('e')

    if grid[px - 1][py] == '.':
        actions_ls.append('n')
    if grid[px][py - 1] == '.':
        actions_ls.append('w')
    if px < len(grid):
        if grid[px + 1][py] == '.':
            actions_ls.append('s')
    if py < len(grid[0]):
        if grid[px][py + 1] == '.':
            actions_ls.append('e')
    return actions_ls

def is_goal(state):         #test to see if a state is the goal state
        if (state.goals == []):
            return True
        return False

def dfs(state,n):           #run Depth First Search on a state with a limit of n
    return r_dfs(state,n)

def r_dfs(state,limit):     #recursive DFS
    if is_goal(state):
        return (list(state.grid),int(state.path_cost))
    elif limit == 0:
        return None
    else:
        cutoff_occured = False
        for action in get_actions(state):
            child = transition_function(action,state)
            result = r_dfs(child,limit-1)
            if result == None:
                cutoff_occured = True
            elif result != None:
                return result
        if cutoff_occured == True:
            return None
        else:
            return None


# RUN PROGRAM FROM HERE #
def single_dfs(url):
    grid = parse_file(url)
    print('--- RESULT ---')
    print('Goals at: '+ str(count_goals(grid)))

    start_xy = player_start(grid)

    first_state = State_instance(grid,0,start_xy[0],start_xy[1],count_goals(grid))
    end_state = dfs(first_state,1000)
    print('Path Cost: ' + str(end_state[1]))
    print('Goal State Map: ')
    print_grid(end_state[0])

single_dfs('data/1prize-medium.txt')
single_dfs('data/1prize-large.txt')
#single_dfs('1prize-open.txt')
