import math
from prioritymap import prioritymap
import numpy as np
from collections import defaultdict
import pygame

def best_path(camefrom, current):
    path = {current}
    while current in camefrom.Keys:
        current = camefrom[current]
        path.add(current)
    return path


def astar(start, goal, heuristic_function, edges, vertices):
    openset = prioritymap()

    openset.insert(heuristic_function(start, goal), {start})
    closedset = {}
    previous = {}

    fscore = defaultdict(lambda: float('inf'))
    fscore[start] = heuristic_function(start, goal)

    gscore = defaultdict(lambda: float('inf'))
    gscore[start] = 0

    while len(openset) > 0:
        currentkey, currentmins = openset.min()
        current = currentmins.pop()
        if len(currentmins) == 0:
            openset.pop()
        if current == goal:
            return best_path(previous, current)

        possible_paths = neighbors(current, vertices, edges)

        for item in possible_paths:
            temp = gscore[current] + cost(current, item)
            if temp < gscore[item]:
                gscore[item] = temp
                fscore[item] = gscore[item] + heuristic_function(item, goal)
                previous[item] = current
                if fscore[item] in openset:
                    openset[fscore[item]].add(item)
                else:
                    openset.insert(fscore[item], item)

    return False

def neighbors(current, vertices, edges):
    possible = []
    for vertex in vertices:
            for edge in edges:
                if seg_intersect(current, vertex, edge[0], edge[1]):
                    possible.append(vertex)

    return possible


def cost(current, vertex):
    costly = math.sqrt(math.pow((current[0] - vertex[0]), 2) + math.pow((current[1] - vertex[1]), 2))
    return costly


def perp(a):
    b = np.empty_like(a)
    b[0] = -a[1]
    b[1] = a[0]
    return b


def seg_intersect(a1, a2, b1, b2):
    a1 = np.array(a1)
    a2 = np.array(a2)
    b1 = np.array(b1)
    b2 = np.array(b2)
    da = a2 - a1
    db = b2 - b1
    dp = a1 - b1
    dap = perp(da)
    denom = np.dot(dap, db)
    num = np.dot(dap, dp)
    return (num / denom.astype(float)) * db + b1


def heuristic(current, goal):
    h_score = math.sqrt(math.pow((goal[0] - current[0]), 2) + math.pow((goal[1] - current[1]), 2))

    return h_score