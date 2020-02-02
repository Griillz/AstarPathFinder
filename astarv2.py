import heapq
import pygame
import math
import numpy as np
from collections import defaultdict
from gui import shapes


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
    for shape in shapes:
        i = 1
    return possible


def onsegment(p, q, r):
    if p[0] <= max(p[0], r[0]) and q[0] >= min(p[0], r[0]) and \
            q[1] <= max(p[1], r[1]) and q[1] >= min(p[1], r[1]):
        return True

    return False


def orientation(p, q, r):
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])

    if val == 0:
        return 0
    if val > 0:
        return 1
    if val < 0:
        return 2


def dointersect(p1, q1, p2, q2):
    o1 = orientation(p1, q1, p2)
    o2 = orientation(p1, q1, q2)
    o3 = orientation(p2, q2, p1)
    o4 = orientation(p2, q2, q1)

    if o1 != o2 and o3 != o4:
        return True

    if o1 == 0 and onsegment(p1, p2, q1):
        return True
    if o1 == 0 and onsegment(p1, q2, q1):
        return True
    if o1 == 0 and onsegment(p2, q2, q1):
        return True
    if o1 == 0 and onsegment(p2, q1, q2):
        return True

    return False
