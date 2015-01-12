"""
There are a row of houses, each house can be painted with three colors red, blue and green. 
The cost of painting each house with a certain color is different. You have to paint all 
the houses such that no two adjacent houses have the same color. You have to paint the houses
with minimum cost.
"""

def calculate_painting_cost():
    base_cost = [[7, 5, 4],
                 [3, 6, 1],
                 [8, 7, 4],
                 [6, 2, 9],
                 [1, 4, 7],
                 [2, 3, 6]]
    prev_cost = [0 for col in xrange(3)]
    curr_cost = [0 for col in xrange(3)]
    # calculated_cost = [[0 for col in xrange(3)] for row in xrange(len(base_cost) + 1)]
    for row in xrange(1, len(base_cost)+1):
        # calculated_cost[row][0] = min(calculated_cost[row-1][2], calculated_cost[row-1][1]) + base_cost[row-1][0]
        # calculated_cost[row][1] = min(calculated_cost[row-1][0], calculated_cost[row-1][2]) + base_cost[row-1][1]
        # calculated_cost[row][2] = min(calculated_cost[row-1][0], calculated_cost[row-1][1]) + base_cost[row-1][2]
        curr_cost[0] = min(prev_cost[2], prev_cost[1]) + base_cost[row-1][0]
        curr_cost[1] = min(prev_cost[0], prev_cost[2]) + base_cost[row-1][1]
        curr_cost[2] = min(prev_cost[0], prev_cost[1]) + base_cost[row-1][2]
        prev_cost = list(curr_cost)
    row = len(base_cost)
    final_cost = min(curr_cost[0], min(curr_cost[1], curr_cost[2]))
    # final_cost = min(calculated_cost[row][0], min(calculated_cost[row][1], calculated_cost[row][2]))
    print final_cost
    # for row in calculated_cost:
    #     print row
if __name__ == '__main__':
    calculate_painting_cost()