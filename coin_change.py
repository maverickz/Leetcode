import sys

def coin_change(denom, target):
    C = [0]*(target+1)
    S = [0]*(target+1)
    coin_idx = -1
    for amount in xrange(1, target+1):
        curr_min = sys.maxint
        for coin in denom:
            if coin <= amount:
                if 1 + C[amount - coin] < curr_min:
                    curr_min = 1 + C[amount - coin]
                    coin_idx = denom.index(coin)
        C[amount] = curr_min
        S[amount] = coin_idx
        print_coins(denom, S, amount)
    


def print_coins(denom, S, target):
    print target, ':',
    while target > 0:
        if S[target] < 0:
            break
        print denom[S[target]],
        target = target - denom[S[target]]
    print

if __name__ == '__main__':
    coin_change([2,3,5,6], 10)

