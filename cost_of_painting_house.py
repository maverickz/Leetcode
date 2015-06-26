cost_matrix = [[7, 5, 10],
              [3, 6, 1],
              [8, 7, 4],
              [6, 2, 9],
              [1, 4, 7],
              [2, 3, 6],
             ]

def find_min_cost(cost_matrix):
    l = len(cost_matrix)
    R = 0
    G = 1
    B = 2
    cum_cost = [0]*len(cost_matrix[0])
    curr_cost = [0]*len(cost_matrix[0])
    cum_cost[R] = cost_matrix[0][R]
    cum_cost[G] = cost_matrix[0][G]
    cum_cost[B] = cost_matrix[0][B]

    for row in xrange(1, l):
        curr_cost[R] = min(cum_cost[G], cum_cost[B]) + cost_matrix[row][R]
        curr_cost[G] = min(cum_cost[R], cum_cost[B]) + cost_matrix[row][G]
        curr_cost[B] = min(cum_cost[R], cum_cost[G]) + cost_matrix[row][B]
        cum_cost = curr_cost[:]
    return min(cum_cost[R], min(cum_cost[G], cum_cost[B]))

assert(find_min_cost(cost_matrix) == 18)




