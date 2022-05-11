#findLowestCostNode() function to find the lowest cost in the graph

def findLowestCostNode(costs):
    lowestCost = float("inf")
    lowestCostNode = None
    for node in costs:
        cost = costs[node]
        if cost < costs[node] and node not in processed:
            lowestCost = cost
            lowestCostNode = node
    return lowestCostNode

#first hash table for dijkstra's algorithm which is graph

graph ={}
graph["start"] = {}             #nested hash table
graph["start"]["a"] = 6         #weight from start to node a
graph["start"]["b"] = 2         #weight from start to node b
graph["a"] = {}
graph["b"]["a"] = 3
graph["b"]["finish"] = 5
graph["finish"] = {}

#second hash table for dijkstra's algorithm which is costs of nodes

infinity = float("inf")         #this line is to define & assign infinity in python

costs ={}
costs["a"] = 6
costs["b"] = 2
costs["finish"] = infinity

#third hash table of dijkstra's algorithm which is parents of nodes

parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["finish"] = None

#an array for previously processed nodes

processed = []

#dijkstra's algorithm action code

node = findLowestCostNode(costs)    #node is 'B'
while node is not None:
    cost = costs[node]              #cost of 'B' equal 2
    neighbors = graph[node]         #neighbors is a hash table
    for n in neighbors.keys():      #a list of nodes : 'A' , 'finish' and n is 'A'
        newCost = cost + neighbors[n]       #cost of 'B' + weight from 'B' to 'A'
        if cost[n] > newCost:  
            costs[n] = newCost      #old cost of 'A' is 6, but now is 5
            parents[n] = node       #set 'B' as the new parent of 'A'
    processed.append(node)          #mark the node as processed
    node = findLowestCostNode(costs)        #find the next lowest cost node and loop the process
    