import math
import prioritymap
import numpy as np
import pygame


def astar(start, goal, heuristic_function, edges, vertices):

    openset = prioritymap()

    openset.insert(start, 0)
    closedset = {}
    previous = {}
    openset.heappush
    cost = {}
    cost[start] = 0

    fscore = {}
    fscore[start] = heuristic_function(start, goal)

    while len(openset) > 0:
        current = openset[0]



def neighbors(current, vertices, edges, closed):
    possible = []
    for i in range(len(vertices)):
        if vertices[i] not in closed:
            for j in range(len(edges)):
                xdiff = (current[0][0] - vertices[i][0], edges[j][0][0] - edges[j][1][0])
                ydiff = (current[0][1] - vertices[i][1], edges[j][0][1] - edges[j][1][1])

                def det(one, two):
                    return one[0] * two[1] - one[1] * two[0]

                div = det(xdiff, ydiff)
                if div == 0:
                    possible.append(vertices[i])
    return possible

def heuristic(current, goal):
    h_score = math.sqrt(math.pow((goal[0] - current[0]), 2) + math.pow((goal[1] - current[1]), 2))

    return h_score
