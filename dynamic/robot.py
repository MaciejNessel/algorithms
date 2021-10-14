# The robot moves through a two-dimensional labyrinth and is supposed to go from  A = (xa, ya) to position B = (xb, yb).
# The robot can make the following movements:
#    1.move forward to the next square,
#    2.rotate 90 degrees clockwise,
#    3. 90 degree rotation counterclockwise.
#
# It takes 45 seconds for the robot to rotate.
#
# While moving forward, the robot accelerates and overcomes the first field takes 60 seconds,
# the second one 40 seconds, and the next one 30 seconds field.
# Performing a rotation stops the robot and the following forward movements return it speed up.
#
#Find the minimum time needed to complete the labirynth

from queue import PriorityQueue
from math import inf


def robot(labyrinth, start_point, end_point):
    # Moving the robot to the right, down, left, up
    r = [[0, 1], [1, 0], [0, -1], [-1, 0]]

    # Travel time during 1st, 2nd, 3rd movement; additional turnover time is 45s.
    cost = [60, 40, 30]

    f = [[[[inf for a in range(3)]  # 3 steps with a different price
            for b in range(4)]  # 4 directions to get to the cell
            for c in range(len(labyrinth[0]))]  # position x
            for d in range(len(labyrinth))]  # position x

    pq = PriorityQueue()
    pq.put((0, start_point[1], start_point[0], 0, 0))

    while pq.qsize() > 0:
        res, x, y, prev, v = pq.get()

        if (y, x) == end_point:
            return res
        if f[x][y][prev][v] != inf:
            continue

        f[x][y][prev][v] = res

        pq.put((res + 45, x, y, (prev + 1) % 4, 0))
        pq.put((res + 45, x, y, (prev + 3) % 4, 0))

        x += r[prev][0]
        y += r[prev][1]

        if labyrinth[x][y] == 'X':
            continue
        else:
            pq.put((res + cost[v], x, y, prev, min(v + 1, 2)))

    return None


# Example:
l = [ "XXXXXXXXXXXXXXXXXXXX",
      "X      X           X",
      "X    X     X    X  X",
      "X X     X          X",
      "X   X       X     XX",
      "XX       X     X   X",
      "X    X       X     X",
      "X         X        X",
      "X     X       X    X",
      "XXXXXXXXXXXXXXXXXXXX"]
a = (1, 1)
b = (18, 8)

result = robot(l, a, b)

if result is not None:
    print("Result value: ", result)
else:
    print("None")