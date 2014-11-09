def longest_subseq_sum(array):
    l = len(array)
    current_max = array[0]
    final_max = array[0]
    start = 0
    end = 0
    temp_start = 0

    for i in xrange(1,l):
        if current_max < 0:
            current_max = array[i]
            temp_start = i
        else:
            current_max += array[i]
        if current_max > final_max:
            final_max = current_max
            start = temp_start
            end = i
    print final_max

longest_subseq_sum([1,2,-3,-4])

        