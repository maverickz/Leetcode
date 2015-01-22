def find_duplicates(array):
    lo = 1
    hi = len(array) - 1

    while lo < hi:
        print lo, hi
        mid = lo + ((hi-lo)/2)
        lo_lo = lo
        lo_hi = mid
        hi_lo = mid+1
        hi_hi = hi

        lo_range_count = 0

        for elem in array:
            if elem >= lo_lo and elem <= lo_hi:
                lo_range_count += 1

        lo_range_expected = lo_hi - lo_lo + 1
        print "Exp", lo_range_count, lo_range_expected
        print lo_lo, lo_hi, hi_lo, hi_hi

        if lo_range_count > lo_range_expected:
            lo, hi = lo_lo, lo_hi
        else:
            lo, hi = hi_lo, hi_hi


    return lo


print find_duplicates([1,3,1,2])

