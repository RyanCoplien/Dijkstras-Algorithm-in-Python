#-----------------------------------------------------------------------
# Name: Ryan Coplien
# Project: LinkState Dijkstra Algorithm
# Course: 3830 Data Communications and Computer Networking
#-----------------------------------------------------------------------
import csv
import sys
import heapq as hq
from collections import defaultdict

results = []
nodes = 0
distanceList = []
costList = []


# Implementation of the Dijkstra's algorithm taking in the edges, the starting node
# and which node you want to go to
# returns: cost and path to the to_node
def dijkstra(edges, from_node, to_node):

    graph = defaultdict(list)
    # f = from node
    # t = to node
    # c = the cost between the nodes
    for f, t, c in edges:
        graph[f].append((c, t))
        graph[t].append((c, f))

    # pushes the first node to the queue
    queue = [(0.0, from_node, ())]
    # creates the visited and distance arrays to zero
    visited = set()
    distance = {from_node: 0}

    while queue:
        # Pops the node
        (cost, node1, path) = hq.heappop(queue)

        # if we have already been here then skip
        if node1 in visited:
            continue

        visited.add(node1)

        # Saving the path
        path += (node1,)

        for c, node2 in graph.get(node1, ()):
            c = float(c)

            # if we have already been here then skip
            if node2 in visited:
                continue

            # if no distance is found or a cheaper cost is found then it replaces it
            if node2 not in distance or cost + c < distance[node2]:
                distance[node2] = cost + c
                # Pushes the next node to the heap
                hq.heappush(queue, (float(cost + c), node2, path))

        # The end case of the loop returning the path and cost
        if node1 == to_node:
            return cost, path

    return -1


# This opens the file and formats it in order to be read properly
with open(str(sys.argv[1]), newline='') as f:
    reader = csv.reader(f, delimiter=' ')
    firstLine = True
    for row in reader:
        if firstLine:
            firstLine = False
            nodes = row
        else:
            # converts to a tuple from an array
            results.append(tuple(row))

# Takes start node from the parameters
start_node = str(sys.argv[2])

# Loops through each of the nodes from the one node
for i in [x for x in range(int(nodes[0])) if x != int(start_node)]:
    # runs the algorithm and takes the results to be formatted
    costs, paths = dijkstra(results, start_node, str(i))

    if costs >= 0:
        output = ""
        for p in paths:
            output += str(p) + '->'

        output = output[:-2] # removes the bonus arrow because I was lazy
        
    else:
        # If the path is not found
        costs = "N/A"
        paths = "N/A"
    
    print("shortest path to node " + str(i) + " is " + str(output) + " with cost: " + str(costs))
