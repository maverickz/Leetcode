from collections import defaultdict

def is_isomorphic(str1, str2):
    l1 = len(str1)
    l2 = len(str2)
    if l1 != l2:
        return False

    map1 = {}
    map2 = {}

    for char in str1:
        if char in map1:
            map1[char] += 1
        else:
            map1[char] = 1

    for char in str2:
        if char in map2:
            map2[char] += 1
        else:
            map2[char] = 1

    if len(map1) != len(map2):
        return False

    l1 = sorted(map1.values())
    l2 = sorted(map2.values())

    print l1, l2
    for i in xrange(len(l1)):
        if l1[i] != l2[i]:
            return False

    return True


assert(is_isomorphic("foo", "app") == True)









