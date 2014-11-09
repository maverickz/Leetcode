import heapq
"""
    The method implements a data structure, which supports the following 
    operations: 
       - insert and remove in O(log N) 
       - find the median in O(1), 
    where N is the number of elements in the data structure.

    Left is a Max-Heap.
    Right is a Min-Heap.
    Insertion is done as follows:

    - If the new element x is smaller than the root of Left then we insert x to Left
    - Else we insert x to Right
    - If after insertion Left and Right differ in the number of elements by more than 1, 
      then we call Extract-Max on Left and insert it to Right
    - Else if after insertion Right has count of elements that is greater than the count 
      of elements of Left, then we call Extract-Min on Right and insert it to Left
    The median is always the root of Left
"""
def find_median(l):
    left = []
    right = []
    for elem in l:
        if not len(left) and not len(right):
            heapq.heappush(left, -elem)
            continue
        if elem < abs(left[0]):
            heapq.heappush(left, -elem)
        else:
            heapq.heappush(right, elem)

        if len(left) > len(right) and (len(left) - len(right)) > 1:
            max_elem = abs(heapq.heappop(left))
            heapq.heappush(right, max_elem)
        elif len(right) > len(left):
            min_elem = heapq.heappop(right)
            heapq.heappush(left, -min_elem)

    return abs(left[0])


if __name__ == '__main__':
    l = [1,3,4,2,5,8,9,10,7,9]
    print find_median(l)
