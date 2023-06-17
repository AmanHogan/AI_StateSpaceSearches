import file2puzzle as f2p
import breadth as b
import depth as d
import uniform as u
import greedy as g
import nodes as n
import a_star as a
import depth_limited as dl
import iterative_deep as i
import sys
sys.setrecursionlimit(1000000)

start_file = None
goal_file = None
method = None
dump_flag = None
depth_limit = None
init_state = None
goal_state = None

# if 4 > len(sys.argv) >= 1:
    #print(f'Missing Command Line arguments: Args: \n{sys.argv}')
    #exit(-1)

# try:
    #start_file = sys.argv[1]
    #goal_file = sys.argv[2]
    #method = sys.argv[3]
    #dump_flag = sys.argv[4]
    #depth_limit = sys.argv[5]

# except IndexError as e:
    # pass

start_file = 'start.txt'
goal_file = 'goal.txt'
method = 'dfs'
dump_flag = 'false'


init_state = f2p.create_puzzle(start_file)
goal_state = f2p.create_puzzle(goal_file)

if method == 'bfs':
    # Breadth First Search
    goal_node = b.bfs(init_state, goal_state, sys.argv, dump_flag)
    if goal_node == -1:
        print('No solution was found or at some point the fringe became empty')
        exit(0)
    n.find_goal_path(goal_node)
    n.print_path_details()

elif method == 'dfs':
    # Depth First Search
    goal_node = d.dfs(init_state, goal_state, sys.argv, dump_flag)
    if goal_node == -1:
        print('No solution was found or at some point the fringe became empty')
        exit(0)
    n.find_goal_path(goal_node)
    print('Finished')
    n.print_path_details_dfs()

elif method == 'ucs':
    # Uniform Cost Search
    goal_node = u.ucs(init_state, goal_state, sys.argv, dump_flag)
    if goal_node == -1:
        print('No solution was found or at some point the fringe became empty')
        exit(0)
    n.find_goal_path(goal_node)
    n.print_path_details()

elif method == 'greedy':
    # Greedy Search
    goal_node = g.greedy(init_state, goal_state, sys.argv, dump_flag)
    if goal_node == -1:
        print('No solution was found or at some point the fringe became empty')
        exit(0)
    n.find_goal_path(goal_node)
    n.print_path_details()

elif method == 'a*':
    # A * Search
    goal_node = a.a_s(init_state, goal_state, sys.argv, dump_flag)
    if goal_node == -1:
        print('No solution was found or at some point the fringe became empty')
        exit(0)
    n.find_goal_path(goal_node)
    n.print_path_details()

elif method == 'dls':
        # Depth-Limited Search
        goal_node = dl.dls(init_state, goal_state, sys.argv, dump_flag, int(depth_limit))
        if goal_node == -1:
            print('No solution was found or at some point the fringe became empty')
            exit(0)
        n.find_goal_path(goal_node)
        n.print_path_details()

elif method == 'ids':
        # Depth-Limited Search
        max_depth = int(depth_limit)
        goal_node = i.ids(init_state, goal_state, sys.argv, dump_flag, max_depth)
        if goal_node == -1:
            print('No solution was found or at some point the fringe became empty')
            exit(0)
        n.find_goal_path(goal_node)
        n.print_path_details()


