def find_smallest_substr_with_target(src, target):
    if not src:
        return None

    char_map = {}
    for char in target:
        if char in char_map:
            char_map[char] += 1
        else:
            char_map[char] = 1

    zero_count = 0
    num_unique_char = len(char_map)
    window = []
    output = []

    for i in xrange(len(src)):
        char = src[i]
        if len(window) >= len(target):
            removed_char = window.pop(0)
            if removed_char in char_map:
                if char_map[char] == 0:
                    zero_count -= 1
                char_map[removed_char] += 1

        window.append(char)

        if char in char_map and char_map[char] > 0:
            char_map[char] -= 1
            if char_map[char] == 0:
                zero_count += 1

        if zero_count == num_unique_char:
            print i, i - len(window) + 1
            output.append(''.join(window))

    print output


find_smallest_substr_with_target('bacbd', 'bcd')



                                                                                                    
