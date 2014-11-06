def longest_plaindrome(string):
    if string is None or not len(string):
        print "Null string"
    size = len(string)
    longest_len = 1
    start_index = 0
    for i in xrange(size):
        j = k = i
        while j>=0 and k < size and string[j] == string[k]:
            current_longest = k - j + 1
            j -= 1
            k += 1
        if current_longest > longest_len:
            longest_len = current_longest
            start_index = j+1
        print longest_len, current_longest, start_index

        j = i
        k = i+1
        while j>=0 and k < size and string[j] == string[k]:
            current_longest = k - j + 1
            j -= 1
            k += 1
        if current_longest > longest_len:
            longest_len = current_longest
            start_index = j+1
        print longest_len, current_longest, start_index
    if string:
        print string[start_index:start_index+longest_len]


          
            