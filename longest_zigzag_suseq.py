"""
	Problem Statement
	    	
	A sequence of numbers is called a zig-zag sequence if the differences between successive numbers strictly alternate between positive and negative. The first difference (if one exists) may be either positive or negative. A sequence with fewer than two elements is trivially a zig-zag sequence.

	For example, 1,7,4,9,2,5 is a zig-zag sequence because the differences (6,-3,5,-7,3) are alternately positive and negative. In contrast, 1,4,7,2,5 and 1,7,4,5,5 are not zig-zag sequences, the first because its first two differences are positive and the second because its last difference is zero.

	Given a sequence of integers, sequence, return the length of the longest subsequence of sequence that is a zig-zag sequence. A subsequence is obtained by deleting some number of elements (possibly zero) from the original sequence, leaving the remaining elements in their original order.

	 
	Definition
	    	
	Class:	ZigZag
	Method:	longestZigZag
	Parameters:	int[]
	Returns:	int
	Method signature:	int longestZigZag(int[] sequence)
	(be sure your method is public)
	    
	 
	Constraints
	-	sequence contains between 1 and 50 elements, inclusive.
	-	Each element of sequence is between 1 and 1000, inclusive.
	 
	Examples
	0)	
	    	
	{ 1, 7, 4, 9, 2, 5 }
	Returns: 6
	The entire sequence is a zig-zag sequence.
	1)	
	    	
	{ 1, 17, 5, 10, 13, 15, 10, 5, 16, 8 }
	Returns: 7
	There are several subsequences that achieve this length. One is 1,17,10,13,10,16,8.
	2)	
	    	
	{ 44 }
	Returns: 1

	Solution:
	    Let A be the array of numbers
		Let up(i) be the length of the longest Zigzag susbseq ending in i and increasing
		Let down(i) be the length of the longest Zigzag susbseq ending in i and decreasing
		Boundary conditions:
		    up(0) = down(0) = 1

		Optimal solution:
		    up(i) = Max(down(j) for all j<i and A[i] > A[j]) + 1
		    down(i) = Max(up(j) for all j<i and A[j] > A[i]) + 1
"""
def longest_zigzag_suseq(array):
	up = [0]*len(array)
	down = [0]*len(array)
	up[0] = down[0] = 1

	for i in xrange(len(array)):
		for j in xrange(i):
			if array[i] > array[j] and up[i] < down[j]:
				up[i] = down[j] + 1
			if array[j] > array[i] and down[i] < up[j]:
				down[i] = up[j] + 1

	return max(up) if max(up) > max(down) else max(down)

if __name__ == '__main__':
	array = [1, 17, 5, 10, 13, 15, 10, 5, 16, 8]
	print longest_zigzag_suseq(array)

