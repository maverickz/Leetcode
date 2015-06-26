'''
Square sum:
12=2^2+2^2+2^2 (not 3^2+1^2+1^2+1^2) output: {2 2 2} 
'''

def square_sum(N):
    l = int(N**0.5)
    min_count = N
    num = 1

    for i in range(l, 0, -1):
        x = float(N)/(i*i)
        y = N/(i*i)
        if float(y) == x:
            if min_count > y:
                num = i
                min_count = y
    print str(num)*min_count

square_sum(18)
               