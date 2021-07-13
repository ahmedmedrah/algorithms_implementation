graph = {}
graph["start"] = {}
graph["start"]["a"] = 5
graph["start"]["b"] = 2

graph["a"] = {}
graph["a"]["c"] = 4
graph["a"]["d"] = 2

graph["b"] = {}
graph["b"]["a"] = 8
graph["b"]["d"] = 7

graph["c"] = {}
graph["c"]["d"] = 6
graph["c"]["fin"] = 3

graph["d"] = {}
graph["d"]["fin"] = 1

graph["fin"] = {}




def dijkstra(start,end,graph):
    infinity = float("inf") 

    # create the costs table      
    def create_costs():
        costs = {}        
        for n in graph.keys():   
            # set the costs of start neighbors else infinity
            if n in graph[start]:                         
                costs[n] = graph[start][n]
            else:    
                costs[n] = infinity
        costs[start] = 0  
        return costs 
    costs = create_costs()

    # create the parents table
    def create_parents():
        parents = {}
        # set the parents of the neighbors of start to start
        for n in graph[start]:
            parents[n] = start
        # start and end has no parents yet    
        parents[end] = None
        parents[start] = None
        return parents
    parents = create_parents()    

    # already visited nodes
    processed = []

    # search for the lowest cost node that has not yet been visited
    def find_lowest_cost_node():
        lowest_cost = infinity
        lowest_cost_node = None
        for node in costs.keys():
            if not node in processed:
                if costs[node] < lowest_cost:
                    lowest_cost = costs[node]
                    lowest_cost_node = node
        return lowest_cost_node
    node = find_lowest_cost_node()

    # while there is a node to process
    while node is not None:        
        cost = costs[node]
        # get its neighbors
        neighbors = graph[node]
        for n in neighbors.keys():
            new_cost = cost + neighbors[n]
            # If it's cheaper to get to this neighbor by going through this node
            # update the cost and the parent
            if costs[n] > new_cost:                
                costs[n] = new_cost
                parents[n] = node
        # mark it as visited        
        processed.append(node)
        # find the next lowest node
        node = find_lowest_cost_node()

    current = end
    path = []
    # create the path by backtracking the parents
    while current != None:
        path.append(current)
        current = parents[current]        
    return costs, parents, list(reversed(path))    


costs, parents, path = dijkstra('start','fin',graph)
for i in range(len(path)):
    print(path[i],'=>' * (path[i] != path[-1]),end=' ')