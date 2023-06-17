import eight as e
import nodes as n


def ucs(initial_state, goal_state, arguments, dump_flag):
    f = None

    if dump_flag == 'true':
        f = open("output.txt", "w")
        n.log_root_to_output(f, arguments)

    # Queue to keep track of nodes and visited nodes
    fringe = []
    visited = set()

    # Get initial state - node, and keep track of max fringe size
    root = n.Node(initial_state)
    n.max_fringe_size = len(fringe)

    # Add initial node to fringe and visited set
    fringe.append(root)
    visited.add(tuple(root.state))

    # Dictionary to store the path cost of each state discovered
    path_cost = {tuple(root.state): 0}

    # While the queue is not empty ...
    while fringe:

        # Sort the fringe based on cumulative path cost
        fringe.sort(key=lambda x: x.cum_cost)

        # Pop node from queue
        node = fringe.pop(0)
        n.nodes_popped = n.nodes_popped + 1

        # If node - state matches the goal state ...
        if e.goal_test(node, goal_state):

            # Return goal node - state and close output file
            print('Goal state found')
            if dump_flag == 'true':
                f.close()
            return node

        # Expand node and generate children nodes, log number of nodes popped
        node.children = e.generate_next_states(node)
        n.nodes_expanded = n.nodes_expanded + 1

        if dump_flag == 'true':
            # Log node details to output file
            n.log_node_to_output(f, node, fringe, visited)

        # For each child node ...
        for next_node in node.children:

            # make child node's parent equal to current node
            next_node.parent = node

            # If the next node has not been visited ...
            if tuple(next_node.state) not in visited:
                # Add node to fringe and visited set
                fringe.append(next_node)
                visited.add(tuple(next_node.state))

                # Log maximum fringe size
                if len(fringe) > n.max_fringe_size:
                    n.max_fringe_size = len(fringe)

                # Update path cost, cumulative path cost, and relative path cost
                path_cost[tuple(next_node.state)] = path_cost[tuple(node.state)] + next_node.state[node.state.index(0)]
                next_node.cum_cost = path_cost[tuple(next_node.state)]
                next_node.rel_cost = next_node.state[node.state.index(0)]
                next_node.node_depth = node.node_depth + 1

    # No goal state found or fringe is empty
    print('No solution or fringe was empty')
    return -1
