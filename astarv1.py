import heapq
import pygame
import math
import time
from node import Node
from shape import screen, screen_size, scalex, scaley
from init import *


start_fixed = ((2 * scalex, 18 * scaley))
end_fixed = ((34 * scalex, 3 * scaley))
RED = (255, 0, 0)
GREEN = (0,255,0)

def simplified_anytime(start, goal, points, w, changew, size, gridcopy):
    newcost, openset, incumbent = math.inf, [], []
    times = 0
    last = False
    start_node = Node(None, start)
    start_node.g = start_node.h = start_node.f = 0

    heapq.heappush(openset, (start_node.f, start_node))

    while len(openset) > 0 and not last:
        if w == 1:
            last = True
        newsolution = a_star(start, goal, points, size, w, newcost, openset)
        if newsolution is not None:
            incumbent = newsolution[0]
            print(incumbent)
            newcost = newsolution[1]
        else:
            return incumbent
        for point in incumbent:
            pygame.draw.rect(screen,
                             GREEN,
                             [(MARGIN + WIDTH) * point[1] + MARGIN,
                              (MARGIN + HEIGHT) * point[0] + MARGIN,
                              WIDTH,
                              HEIGHT])
            pygame.event.pump()
        pygame.display.update()
        time.sleep(2)
        screen.fill(BLACK)
        for row in range(gridsize):
            for column in range(gridsize):
                color = WHITE
                if gridcopy[row][column] == 1:
                    color = BLACK
                elif (row, column) == START:
                    color = GREEN
                elif (row, column) == END:
                    color = RED
                pygame.draw.rect(screen,
                                 color,
                                 [(MARGIN + WIDTH) * column + MARGIN,
                                  (MARGIN + HEIGHT) * row + MARGIN,
                                  WIDTH,
                                  HEIGHT])

        if last:
            time.sleep(6)
        if(w > 1):
            w = w - changew
            for node in openset:
                node[1].f = node[1].g + (node[1].h * w)


        count = 0
        for item in openset:
            count = count + 1
            if openset[count][0] >= newcost:
                del openset[count]
                count = count - 1

        print("hi")


# Main a star algorithm
def a_star(start, goal, points, size, w, costly, open):
    # Create start and end node
    start_node = Node(None, start)
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None, goal)
    end_node.g = end_node.h = end_node.f = 0

    # Initialize both open and closed list
    closedset = []
    openset = open
    # pushes start node onto the open set
    heapq.heappush(openset, (start_node.f, start_node))

    # Expands nodes in open set until there are none left, or the goal is reached
    while len(openset) > 0:
        # Get the current node with the lowest F score
        if len(openset) > (gridsize * gridsize):
            print(len(openset))
        current_node = heapq.heappop(openset)[1]
        closedset.append(current_node)

        # Base case for finding the goal as a possible child
        if current_node.position == end_node.position:
            path = []
            current = current_node
            # Loops through the parents of the nodes back to the starting node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1], current_node.g
        else:
            # Draws the current path being explored in red to make it look cooler
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                pygame.draw.rect(screen,
                                 PURPLE,
                                 [(MARGIN + WIDTH) * current.position[1] + MARGIN,
                                  (MARGIN + HEIGHT) * current.position[0] + MARGIN,
                                  WIDTH,
                                  HEIGHT])
                current = current.parent
                pygame.event.pump()
        # gets list of vertices we can travel to from current position
        children = genchildren(current_node, points, size)

        # add children nodes to open set
        for point in children:
            skip = False
            child_node = Node(current_node, point)
            # calculate scores
            child_node.g = cost(current_node.position, point) + current_node.g
            child_node.h = cost(point, end_node.position)
            child_node.f = child_node.g + (child_node.h * w)

            # check if node in open or closed set
            for node in openset:
                if child_node == node[1]:
                    skip = True
                    if child_node.g > node[1].g:
                        continue
                    else:
                        child_node.g = node[1].g
                        continue

            for node in closedset:
                if child_node == node:
                    skip = True
                    continue

            if skip:
                continue
            heapq.heappush(openset, (child_node.f, child_node))

    return None



# Function for getting all possible children we can travel to at the current position

def genchildren(current, points, size):
    possible = []
    x = current.position[0]
    y = current.position[1]

    if x == 0 and y == 0:
        if points[x + 1][y] == 0:
            possible.append((x + 1, y))

        if points[x + 1][y + 1] == 0:
            possible.append((x + 1, y + 1))

        if points[x][y + 1] == 0:
            possible.append((x, y + 1))
    elif x == 0 and y == size:
        if points[x + 1][y] == 0:
            possible.append((x - 1, y))

        if points[x + 1][y - 1] == 0:
            possible.append((x + 1, y - 1))

        if points[x][y - 1] == 0:
            possible.append((x, y - 1))
        #dosomeshit
    elif x == size and y == 0:
        if points[x - 1][y] == 0:
            possible.append((x - 1, y))

        if points[x - 1][y + 1] == 0:
            possible.append((x - 1, y + 1))

        if points[x][y + 1] == 0:
            possible.append((x, y + 1))
        #dosomeshit
    elif x == size and y == size:
        if points[x - 1][y] == 0:
            possible.append((x - 1, y))

        if points[x - 1][y - 1] == 0:
            possible.append((x - 1, y - 1))

        if points[x][y - 1] == 0:
            possible.append((x, y - 1))
        #dosomeshit
    elif x == 0 or x == size:
        if x == 0:
            if points[x][y - 1] == 0:
                possible.append((x, y - 1))

            if points[x + 1][y - 1] == 0:
                possible.append((x + 1, y - 1))

            if points[x + 1][y] == 0:
                possible.append((x + 1, y))

            if points[x + 1][y + 1] == 0:
                possible.append((x + 1, y + 1))

            if points[x][y + 1] == 0:
                possible.append((x, y + 1))
        else:
            if points[x][y - 1] == 0:
                possible.append((x, y - 1))

            if points[x - 1][y - 1] == 0:
                possible.append((x - 1, y - 1))

            if points[x - 1][y] == 0:
                possible.append((x - 1, y))

            if points[x - 1][y + 1] == 0:
                possible.append((x - 1, y + 1))

            if points[x][y + 1] == 0:
                possible.append((x, y + 1))
    elif y == 0 or y == size:
        if y == 0:
            if points[x - 1][y] == 0:
                possible.append((x - 1, y))

            if points[x - 1][y + 1] == 0:
                possible.append((x - 1, y + 1))

            if points[x][y + 1] == 0:
                possible.append((x, y + 1))

            if points[x + 1][y + 1] == 0:
                possible.append((x + 1, y + 1))

            if points[x + 1][y] == 0:
                possible.append((x + 1, y))
        else:
            if points[x - 1][y] == 0:
                possible.append((x - 1, y))

            if points[x - 1][y - 1] == 0:
                possible.append((x - 1, y - 1))

            if points[x][y - 1] == 0:
                possible.append((x, y - 1))

            if points[x + 1][y - 1] == 0:
                possible.append((x + 1, y - 1))

            if points[x + 1][y] == 0:
                possible.append((x + 1, y))
    else:
        #basecase
        if points[x + 1][y] == 0:
            possible.append((x + 1, y))

        if points[x + 1][y + 1] == 0:
            possible.append((x + 1, y + 1))

        if points[x][y + 1] == 0:
            possible.append((x, y + 1))

        if points[x - 1][y + 1] == 0:
            possible.append((x - 1, y + 1))

        if points[x - 1][y] == 0:
            possible.append((x - 1, y))

        if points[x - 1][y - 1] == 0:
            possible.append((x - 1, y - 1))

        if points[x][y - 1] == 0:
            possible.append((x, y - 1))

        if points[x + 1][y - 1] == 0:
            possible.append((x + 1, y - 1))

    return possible

# Cost function for g scores
def cost(current, vertex):
    price = math.sqrt(math.pow((current[0] - vertex[0]), 2) + math.pow((current[1] - vertex[1]), 2))
    return price

# Heuristic function
def heuristic(current, goal):
    h_score = math.sqrt(math.pow((goal[0] - current[0]), 2) + math.pow((goal[1] - current[1]), 2))
    return h_score