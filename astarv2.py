import heapq
import pygame
import math
import time
from node import Node
from shape import screen

RED = (255, 0, 0)

#Main a star algorithm
def a_star(start, goal, vertices, edges, shapes):
    # Create start and end node
    start_node = Node(None, start)
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None, goal)
    end_node.g = end_node.h = end_node.f = 0

    # Initialize both open and closed list
    openset, closedset = [], []

    # pushes start node onto the open set
    heapq.heappush(openset, (start_node.f, start_node))
    num = 0

    #Expands nodes in open set until there are none left, or the goal is reached
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
        else:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            if len(path) > 1:
                pygame.draw.lines(screen, RED, False, path[::-1], 3)
                #time.sleep(.05)
                pygame.display.update()

        # gets list of vertices we can travel to from current position
        children = genchildren(current_node, vertices, edges, shapes, num)
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

    return False


def genchildren(current, vertices, edges, shapes, num):
    possible = []
    for vertex in vertices:
        intersected = False
        permintersect = False
        if current.position != vertex:
            # pygame.draw.line(screen, WHITE, vertex, current[1], 3)
            for edge in edges:
                # pygame.draw.line(screen, WHITE, edge[0], edge[1])
                if intersect(current.position, vertex, edge[0], edge[1]):
                    intersected = True
                    if num != 0:
                        if (vertex in edge or current.position in edge):
                            intersected = False
                            for shape in shapes:
                                if vertex in shape.vertices and current.position in shape.vertices:
                                    if shape.vertices.index(current.position) == len(shape.vertices) - 1:
                                        if not (shape.vertices[0] == vertex or shape.vertices[-2] == vertex):
                                            intersected = True
                                    elif not (shape.vertices[shape.vertices.index(current.position) + 1] == vertex or \
                                              shape.vertices[shape.vertices.index(current.position) - 1] == vertex):
                                        intersected = True
                        else:
                            permintersect = True
                            break
                    else:
                        intersected = True
                        if vertex in edge or current.position in edge:
                            intersected = False
                        else:
                            permintersect = True
                            break

            if not intersected and not permintersect:
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
    price = math.sqrt(math.pow((current[0] - vertex[0]), 2) + math.pow((current[1] - vertex[1]), 2))
    return price


def heuristic(current, goal):
    h_score = math.sqrt(math.pow((goal[0] - current[0]), 2) + math.pow((goal[1] - current[1]), 2))
    return h_score
