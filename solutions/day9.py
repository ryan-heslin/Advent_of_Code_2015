import re
from math import inf 
from itertools import permutations
from collections import defaultdict

with open("inputs/day9.txt") as f: 
    raw_input = f.read().splitlines()

def parse_distances(lines):
    out = defaultdict(dict)
    # Map each parent node to a mapping of neighbors to distances
    for line in lines: 
        node, neighbor, distance = re.match(r"^([a-zA-Z]+) to ([a-zA-Z]+) = (\d+)$", line).groups()
        # Create new mapping for parent node if not yet known
    
        # Since edges are symmetric
        out[node][neighbor] = out[neighbor][node] = int(distance)
    return out


class Node():

    def __init__(self, name : str, neighbors : dict): 
        self.name = name
        self.neighbors = neighbors

    def __hash__(self) ->  int:
        return hash(self.name)

    def __repr__(self):
        return f"{self.name}\n{self.neighbors}"

parsed = parse_distances(raw_input)
graph = [Node(node, neighbors) for node,neighbors in parsed.items()]
positions = {node : i for i, node in enumerate(parsed.keys())}

# Brute force works sometimes
perms = permutations(positions.keys(), len(positions.keys()))

def solve(perms, comparator, start, failure):
    best = start
    for perm in perms:
        distance = 0
        for i, city in enumerate(perm[:-1]):
            index = positions[city]
            distance += graph[index].neighbors.get(perm[i+1], failure)
            # If path dead-ends, abandon it
            if distance == failure: 
                break
        else: 
            best = comparator(best, distance)


    return best

part1 = solve(perms, min, inf, inf)
perms = permutations(positions.keys(), len(positions.keys()))
part2 = solve(perms, max, -inf, -inf)
print(part1)
print(part2)




# Algorithm from https://www.baeldung.com/cs/shortest-path-visiting-all-nodes
# Yes, I forgot P probably doesn't equal NP
#V = len(graph)
#permutations = 2 ** V
#cost = {node.name : [inf] * permutations for node in graph }
#queue = deque()
## Add each node to queue (to simulate path starting from it)
#for  i, node in enumerate(graph):
    ##add node, 2^i to Q 
    #power = 2 ** i
    #queue.appendleft([ node, power ])
    ## Cost from node to itself is 0
    #cost[node.name][power] = 0
#while queue:
    ## Bitmask stores indices of nodes visited to get to each node
    #current_node, current_bitmask = queue.popleft()
    #for  neighbor, distance in current_node.neighbors.items(): 
        ##distance = current_node.neighbors[neighbor]
        #neighbor_index = positions[neighbor] 
        ## Compute cost to visiting neighbor through this node
        #updated_bitmask = current_bitmask | 2 ** neighbor_index
        #if cost[neighbor][updated_bitmask] < inf: 
            #continue
        #updated_cost = cost[current_node.name][current_bitmask] + distance
        #if cost[neighbor][updated_bitmask] > updated_cost:
        ##   Turn on bit of child node to indicate we visited it
            #queue.append([ graph[positions[neighbor]], updated_bitmask])
##           #Update with newly found cheapest cost
            #cost[neighbor][updated_bitmask] = updated_cost
## Find node with cheapest cost to visit all nodes
## Since each bit is on if that node was visited, the one with all bits on indicates complete traverse
#answer = inf
#for i, node in enumerate(graph):
    #answer = min(answer, cost[node.name][permutations - 1])
#print(answer)
#
