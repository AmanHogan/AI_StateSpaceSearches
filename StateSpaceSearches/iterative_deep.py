import eight as e
import nodes as n
import depth_limited as dl
import sys

sys.setrecursionlimit(1000000)


def ids(initial_state, goal_state, arguments, dump_flag, max_depth):
    for depth in range(max_depth+1):
        result = dl.dls(initial_state, goal_state, arguments, dump_flag, depth)
        if result != -1:
            return result
    return -1
