import heapq
import pygame
import math
import numpy as np
from collections import defaultdict
from gui import vertices, edges


def best_path(camefrom, current):
    total_path = {current}

    return total_path


def a_star(start, goal, heuristic):
    openset = [start]
    closedset = []

    camefrom = []

    gscore = defaultdict(lambda: float('inf'))
    gscore[start] = 0

    fscore = defaultdict(lambda: float('inf'))


    fscore[start] = heuristic(start, goal)

    while len(openset) > 0:
        current = heapq.heappop(openset)
        closedset.append(current)

        if current == goal:
            return best_path(camefrom, current)

    return False


def genchildren(current):
    possible = []
    for vertex in vertices:
        for edge in edges:
            #if seg_intersect(current, vertex, edge[0], edge[1]):
                possible.append(vertex)

    return possible