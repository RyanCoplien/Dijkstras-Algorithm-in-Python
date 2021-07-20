#-----------------------------------------------------------------------
# Name: Ryan Coplien
# Project: LinkState Dijkstra Algorithm
# Course: 3830 Data Communications and Computer Networking
#-----------------------------------------------------------------------
import heapq as heapQueue
from collections import defaultdict
import csv
import sys

textParse=[]
currentNode=0

def findShortestPath(edges, firstNode, secondNode):
    chart=defaultdict(list)
    stack=[(0, firstNode, ())]
    length={firstNode: 0}
    nodeSet=set()
    for fromNode, toNode, linkCost in edges:
        chart[toNode].append((linkCost, fromNode))
        chart[fromNode].append((linkCost, toNode))
    while stack:
        (currentCost, startNode, shortPath)=heapQueue.heappop(stack)
        if startNode in nodeSet:
            continue
        nodeSet.add(startNode)
        shortPath += (startNode,)
        for linkCost, endNode in chart.get(startNode, ()):
            linkCost=float(linkCost)
            if endNode in nodeSet:
                continue
            if endNode not in length or currentCost + linkCost < length[endNode]:
                length[endNode]=currentCost + linkCost
                heapQueue.heappush(stack, (float(currentCost + linkCost), endNode, shortPath))
        if startNode == secondNode:
            return currentCost, shortPath
    return -1

with open(str(sys.argv[1]), newline='') as f:
    data=csv.reader(f, delimiter=' ')
    lineOne=True
    for line in data:
        if lineOne:
            lineOne=False
            currentNode=line
        else:
            textParse.append(tuple(line))
startNode=str(sys.argv[2])

for index in [x for x in range(int(currentNode[0])) if x != int(startNode)]:
    costs, paths=findShortestPath(textParse, startNode, str(index))
    if costs > -1:
        output=""
        for path in paths:
            output += str(path) +" -> "
        output=output[:-4]
        print("Shortest path to node " +str(index)+ " is " +str(output)+ " with cost: " +str(costs))
    else:
        print("Shortest Path Not Found")
        break
