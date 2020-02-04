import heapq
import pygame
import math
from node import Node
import numpy as np
from collections import defaultdict
from temporary import screen, WHITE


def a_star(start, goal, heuristic, vertices, edges, shapes):
    # Create start and end node
    start_node = Node(None, start)
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None, goal)
    end_node.g = end_node.h = end_node.f = 0

    # Initialize both open and closed list
    openset, closedset = [], []

    # Add the start node
    heapq.heappush(openset, (start_node.f, start_node))
    num = 0
    while len(openset) > 0:
        # Get the current node
        current_node = heapq.heappop(openset)[1]
        closedset.append(current_node)

        # found the end
        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1]

        # gets points that we can go to
        children = genchildren(current_node, vertices, edges, shapes)
        num += 1

        # add children nodes to open list
        for point in children:
            child_node = Node(current_node, point)
            # calculate scores
            child_node.g = cost(current_node.position, point) + current_node.g
            child_node.h = cost(point, end_node.position)
            child_node.f = child_node.g + child_node.h


            # check if node in open or closed list
            for node in openset:
                if child_node == node[1] and child_node.g > node[1].g:
                    continue

            for node in closedset:
                if child_node == node:
                    continue

            heapq.heappush(openset, (child_node.f, child_node))

def genchildren(node, vertices, edges, shapes):
    possible = []
    for vertex in vertices:
        intersected = False
        for edge in edges:
            # check if intersects
            if intersect(node.position, vertex, edge[0], edge[1]) and vertex not in edge and node.position not in edge:
                intersected = True
        if not intersected and node.position != vertex:
            # check if point is in shape and adjacent
            dissects_shape = False
            for shape in shapes:
                if vertex in shape.vertices and node.position in shape.vertices:
                    if vertex == shape.vertices[-1]:
                        if not(node.position == shape.vertices[-2] or node.position == shape.vertices[0]) and vertex not in possible:
                            dissects_shape = True
                    elif not(node.position == shape.vertices[shape.vertices.index(vertex)+1] or node.position == shape.vertices[shape.vertices.index(vertex)-1]):
                        dissects_shape = True
            if vertex not in possible and not dissects_shape:
                possible.append(vertex)
    return possible


def onSeg(p, q, r):
    if (min(p[0], r[0]) >= q[0] > max(p[0], r[0])) and (min(p[1], r[1]) >= q[1] > max(p[1], r[1])):
        return True
    return False


def ccw(p, q, r):
    val = ((q[1] - p[1]) * (r[0] - q[0])) - ((q[0] - p[0]) * (r[1] - q[1]))
    if val == 0:
        return val
    return 1 if val > 0 else 2


def intersect(p1, p2, p3, p4):
    ccw1, ccw2, ccw3, ccw4 = ccw(p1, p2, p3), ccw(p1, p2, p4), ccw(p3, p4, p1), ccw(p3, p4, p2)

    if ccw1 != ccw2 and ccw3 != ccw4:
        return True

    if ccw1 == 0 and onSeg(p1, p3, p2):
        return True
    if ccw2 == 0 and onSeg(p1, p4, p2):
        return True
    if ccw3 == 0 and onSeg(p3, p1, p4):
        return True
    if ccw4 == 0 and onSeg(p3, p2, p4):
        return True

    return False


def cost(current, vertex):
    return math.sqrt(((current[0] - vertex[0]) ** 2) + ((current[1] - vertex[1]) ** 2))


def heuristic(current, goal):
    return math.sqrt(((current[0] - goal[0]) ** 2) + ((current[1] - goal[1]) ** 2))