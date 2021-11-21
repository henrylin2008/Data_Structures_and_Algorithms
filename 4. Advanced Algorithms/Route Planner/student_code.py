from math import pow, sqrt
from queue import PriorityQueue
from collections import defaultdict

# reference: https://www.redblobgames.com/pathfinding/a-star/introduction.html

def retrieve_path(route, start, goal):
    """ 
    retrieve path from the start to the goal node 
    """
    path = []     
    current_node = goal
    path.append(current_node)
    while current_node != start:
        current_node = route[current_node]
        path.append(current_node)
    path.reverse()
    return path

def euclidean_distance(node1, node2): 
    """
    Calculate eculidean distance between 2 nodes 
    """
    return sqrt(pow((node1[0] - node2[0]), 2) + pow((node1[1] - node2[1]), 2))
    
def shortest_path(M, start, goal):
    """
    shortest path with A* algorithm and priority queue 
    """
    print("shortest path called")
    frontier = PriorityQueue()
    frontier.put(start, 0)
    intersection = M.intersections
    if start == goal: 
        return [start]

    came_from = defaultdict(lambda: "Not visited")
    came_from[start] = None
    path_cost = defaultdict(lambda: "Cost not present")
    path_cost[start] = 0    

    while frontier.qsize() > 0:

        current_node = frontier.get()
        if current_node == goal:
            retrieve_path(came_from, start, goal)

        for neighbor in M.roads[current_node]:
            cost_from_start = path_cost[current_node]
            cost_to_goal = euclidean_distance(intersection[current_node], intersection[neighbor])
            estimate_cost = cost_from_start + cost_to_goal

            if neighbor not in path_cost or estimate_cost < path_cost[neighbor]:
                path_cost[neighbor] = estimate_cost
                frontier.put(neighbor, estimate_cost)
                came_from[neighbor] = current_node

    return retrieve_path(came_from, start, goal)
