import heapq
import pygame
import math
import time
from node import Node
from shape import screen, screen_size, scalex, scaley


start_fixed = ((2 * scalex, 18 * scaley))
end_fixed = ((34 * scalex, 3 * scaley))
RED = (255, 0, 0)
GREEN = (0,255,0)

def simplified_anytime(start, goal, vertices, edges, shapes, w, changew):
    newcost, openset, incumbent = math.inf, [], []

    last = False
    start_node = Node(None, start)
    start_node.g = start_node.h = start_node.f = 0

    heapq.heappush(openset, (start_node.f, start_node))

    while len(openset) > 0 and last == False:
        if w == 1:
            last = True
        newsolution, tempcost = a_star(start, goal, vertices, edges, shapes, w, openset)
        if newsolution is not None:
            newcost = tempcost
            incumbent = newsolution
        else:
            return incumbent
        if(w > 1):
            w = w - changew
        for node in openset:
            if node[1].f >= newcost:
                openset.pop(openset.index(node))

    return incumbent


# Main a star algorithm
def a_star(start, goal, vertices, edges, shapes, w, opensetpassed):
    # Create start and end node
    start_node = Node(None, start)
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None, goal)
    end_node.g = end_node.h = end_node.f = 0

    # Initialize both open and closed list
    closedset = []
    openset = opensetpassed
    # pushes start node onto the open set
    heapq.heappush(openset, (start_node.f, start_node))
    num = 0

    # Expands nodes in open set until there are none left, or the goal is reached
    while len(openset) > 0:
        # Get the current node with the lowest F score
        current_node = heapq.heappop(openset)[1]
        closedset.append(current_node)

        # Base case for finding the goal as a possible child
        if current_node == end_node:
            path = []
            current = current_node
            # Loops through the parents of the nodes back to the starting node
            while current is not None:
                path.append(current.position)
                current = current.parent
            # Returns the best path to the gui file, and then draws to the screen
            screen.fill((0, 0, 0))
            pygame.draw.circle(screen, (0, 255, 0), start_fixed, screen_size[0] // 100)
            pygame.draw.circle(screen, (255, 0, 0), end_fixed, screen_size[0] // 100)
            for shape in shapes:
                shape.draw()
            pygame.draw.lines(screen, GREEN, False, path, 3)
            pygame.display.update()
            time.sleep(1)
            return path[::-1], current_node.g
        else:
            # Draws the current path being explored in red to make it look cooler
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            # if len(path) > 1:
            #     pygame.draw.lines(screen, RED, False, path[::-1], 3)
            #     # time.sleep(.05)
            #     pygame.display.update()

        # gets list of vertices we can travel to from current position
        children = genchildren(current_node, vertices, edges, shapes, num)
        num += 1

        # add children nodes to open set
        for point in children:
            child_node = Node(current_node, point)
            # calculate scores
            child_node.g = cost(current_node.position, point) + current_node.g
            child_node.h = cost(point, end_node.position)
            child_node.f = child_node.g + (child_node.h * w)

            # check if node in open or closed set
            for node in openset:
                if child_node == node[1] and child_node.g > node[1].g:
                    continue

            for node in closedset:
                if child_node == node:
                    continue
            heapq.heappush(openset, (child_node.f, child_node))

    return False



# Function for getting all possible children we can travel to at the current position

def genchildren(current, vertices, edges, shapes, num):
    possible = []
    # Loops through all vertices
    for vertex in vertices:
        # Flag for intersecting
        intersected = False
        # Flag that if set to true, will cause us to break out of the loop because we know we can not travel to this
        # specific vertex
        permintersect = False
        if current.position != vertex:
            # Loops through edges
            for edge in edges:
                # Checks if the line segment intersects with current edge
                if intersect(current.position, vertex, edge[0], edge[1]):
                    # Sets to true if there is an intersection
                    intersected = True
                    # Flag for first iteration
                    if num != 0:
                        # If the point we intersected is a vertex, reset the intersected flag to false, as we know that
                        # We can travel to vertices
                        if (vertex in edge or current.position in edge):
                            intersected = False
                            # Loops through each shape and checks if the point we interesected with is on the same shape
                            # As our current position, if it is, we check if it is an adjacent vertex. If it is not am
                            # adjacent vertex, we reset the intersected flag to true again, because that means we have
                            # Traveled through the shape which is not allowed
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
            # Conditions needed for adding a vertex as a possible path to be taken
            if not intersected and not permintersect:
                possible.append(vertex)

    return possible

# Next three functions work together in determining if a line segment intersects another, using orientation of three
# Points as the check.
def onsegment(p, q, r):
    if (min(p[0], r[0]) >= q[0] > max(p[0], r[0])) and (min(p[1], r[1]) >= q[1] > max(p[1], r[1])):
        return True
    return False


def orientation(p, q, r):
    val = ((q[1] - p[1]) * (r[0] - q[0])) - ((q[0] - p[0]) * (r[1] - q[1]))
    if val == 0:
        return val
    return 1 if val > 0 else 2


def intersect(p1, p2, p3, p4):
    o1, o2, o3, o4 = orientation(p1, p2, p3), orientation(p1, p2, p4), orientation(p3, p4, p1), orientation(p3, p4, p2)

    if o1 != o2 and o3 != o4:
        return True

    if o1 == 0 and onsegment(p1, p3, p2):
        return True
    if o2 == 0 and onsegment(p1, p4, p2):
        return True
    if o3 == 0 and onsegment(p3, p1, p4):
        return True
    if o4 == 0 and onsegment(p3, p2, p4):
        return True

    return False

# Cost function for g scores
def cost(current, vertex):
    price = math.sqrt(math.pow((current[0] - vertex[0]), 2) + math.pow((current[1] - vertex[1]), 2))
    return price

# Heuristic function
def heuristic(current, goal):
    h_score = math.sqrt(math.pow((goal[0] - current[0]), 2) + math.pow((goal[1] - current[1]), 2))
    return h_score