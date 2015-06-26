def check_anagram_substr(src, target):
    if not src:
        return None
    char_map = {}
    for char in target:
        if char in char_map:
            char_map[char] += 1
        else:
            char_map[char] = 1

    count = 0
    substr = []
    l = len(target)
    for i in xrange(l):
        char = src[i]
        if char in char_map and char_map[char] > 0:
            char_map[char] -= 1
            substr.append(char) 
            count += 1
        if count == len(target):
            print substr

    for i in xrange(l-1,len(src)):
        char = src[i]
        if char in char_map and char_map[char] > 0:
            char_map[char] -= 1
            substr.append(char) 
            count += 1
        if count == len(target):
            print substr





check_anagram_substr('bcbd', 'bcd')

