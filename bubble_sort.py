"""
There are N+1 parking spots, numbered from 0 to N. 
There are N cars numbered from 1 to N parked in various 
parking spots with one left empty. Reorder the cars so 
that car #1 is in spot #1, car #2 is in spot #2 and so on. 
Spot #0 will remain empty. The only allowed operation is 
to take a car and move it to the free spot.
"""
def swap(array, i, j):
	array[0] = array[i]
	array[i] = array[j]
	array[j] = array[0]
	array[0] = 0


def sort_array(array):
    while True:
        swapped = False
        for i in xrange(1, len(array)):
            if array[i-1] > array[i]:
                swap(array, i-1, i)
                swapped = True
        if not swapped:
            break
    return array


if __name__ =='__main__':
	array = [0,3,2,1,4,5,6,8,9,7]
	print sort_array(array)


