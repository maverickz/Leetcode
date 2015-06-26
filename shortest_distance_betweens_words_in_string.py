from collections import defaultdict
import sys

def shortest_dist(list_of_strings, src, dst):
    hash_map = defaultdict(list)
    for i, elem in enumerate(list_of_strings):
        hash_map[elem].append(i)
    
    src_lst = hash_map[src]
    dst_lst = hash_map[dst]
    i = 0
    j = 0
    curr_min = sys.maxint
    while i < len(src_lst) and j < len(dst_lst):
        curr_min = min(curr_min, abs(src_lst[i] - dst_lst[i]))
        if src_lst[i] < dst_lst[j]:
            i += 1
        else:
            j += 1
    return curr_min  
        


list_of_strings = ["the", "quick", "brown", "fox", "quick"]
print shortest_dist(list_of_strings, "fox","the")