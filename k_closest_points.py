from collections import namedtuple
import math
import random

Point = namedtuple('Point', 'x y')

def select(A, k):
    p = random.randint(0,len(A)-1)
    l1 = []
    l2 = []
    pivot = A[p]
    for elem in A:
        if elem < pivot:
            l1.append(elem)
        elif elem > pivot:
            l2.append(elem)
        else:
            pass

    if k < len(l1):
        return select(l1, k)
    elif k > len(A) - len(l2):
        return select(l2, k - (len(A) - len(l2)))
    else:
        return pivot

def calc_distance(p1, p2):
    return math.sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2)

points =  [Point(5,5), Point(-4,3), Point(3,2), Point(1,0), Point(6, -5)]
distance = [calc_distance(p, Point(0,0)) for p in points]
k = 2
p = select(distance, k)
output = []
for i in xrange(len(distance)):
    elem = distance[i]
    if elem <= p:
        output.append(points[i])

print output





