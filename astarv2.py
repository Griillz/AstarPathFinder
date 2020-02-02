import heapq
import pygame
import math
import numpy as np
from collections import defaultdict



def a_star(start, goal, heuristic, shapes):
    total = 0
    openset = []
    heapq.heappush(openset, (0, start))
    closedset = []

    camefrom =[]
    camefrom.append(start)

    gscore = defaultdict(lambda: float('inf'))
    gscore[start] = 0

    fscore = defaultdict(lambda: float('inf'))

    fscore[start] = heuristic(start, goal)

    while len(openset) > 0:
        current = heapq.heappop(openset)
        total += current[0]
        camefrom.append(current[1])
        closedset.append(current[1])

        if current == goal:
            return camefrom

    children = genchildren(current, shapes)

    for child in children:
        for closed in closedset:
            if child == closed:
                continue

        g = cost(current[1], child) + total
        h = heuristic(current[1], goal)
        f = g + h

        for open in openset:
            if child == open[1] and g > open[0]:
                continue

        heapq.heappush(openset, (f, child))
        closedset.append(current[1])
    return False


def genchildren(current, shapes):
    possible = []
    for shape in shapes:
        for vertex in shape.vertices:
            for edge in shape.edges:
                if not dointersect(current[1],vertex,edge[0], edge[1]) and vertex not in possible:
                    possible.append(vertex)
                elif vertex == edge[0] or vertex == edge[1] and vertex not in possible:
                    possible.append(vertex)
    return possible


def onsegment(p, q, r):
    if p[0] <= max(p[0], r[0]) and q[0] >= min(p[0], r[0]) and \
            q[1] <= max(p[1], r[1]) and q[1] >= min(p[1], r[1]):
        return True

    return False


def orientation(p, q, r):
    qy = int(q[1])
    py = int(p[1])
    rx = int(r[0])
    qx = int(q[0])
    px = int(p[0])
    ry = int(r[1])
    val = (qy - py) * (rx - qx) - (qx - px) * (ry - qy)

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

def cost(current, vertex):
    price = math.sqrt(math.pow((current[0] - vertex[0]), 2) + math.pow((current[1] - vertex[1]), 2))
    return price

def heuristic(current, goal):
    h_score = math.sqrt(math.pow((goal[0] - current[0]), 2) + math.pow((goal[1] - current[1]), 2))
    return h_score