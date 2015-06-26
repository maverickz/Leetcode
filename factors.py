import math

def factors(num):
    result = []
    upper_bound = int(math.ceil(math.sqrt(num)))
    for i in xrange(1, upper_bound):
        if num%i == 0:
            print i, num/i

factors(24)