def factor(number, prev_factors=[]):
    if number == 1:
        if len(prev_factors) < 2:
            prev_factors.append(1)
        print '*'.join(map(str, prev_factors))
    else:
        if prev_factors:
            max_factor = min(number, prev_factors[-1])
        else:
            max_factor = number
        for curr_factor in xrange(max_factor, 1, -1):
            if number % curr_factor == 0:
                factor(number/curr_factor, prev_factors + [curr_factor])


