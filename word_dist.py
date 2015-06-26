from collections import defaultdict
import sys

word_map = defaultdict(list)
def preprocess(word_list):
    for i, word in enumerate(word_list):
        word_map[word] += [i]
    
def shortest_dist(src, dst):
    l1 = word_map[src]
    l2 = word_map[dst]
    i = 0
    j = 0
    min_dist = sys.maxint
    while i < len(l1) and j < len(l2):    
        min_dist = min(min_dist, abs(l1[i] - l2[j]))
        if l1[i] < l2[j]:
            i += 1
        else:
            j += 1
    return min_dist


preprocess(["the", "quick", "brown", "fox", "quick"])
assert(shortest_dist( "the", "brown") == 2)
        
    