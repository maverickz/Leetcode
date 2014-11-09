""" 
   Longest increasing subsequence 
   Given a sequence a_1, a_2, ...., a_n, find the largest subset such that for every i < j, a_i < a_j
   Sub problem:
        Let A be the array of integers
        Let L(i) be the longest increasing subsequence ending in i
        L(0) = A(0) => Base condition
        L(i) =  Max(L(j)) for all j<i and A(j) < A(j) i.e tail of the LIS ending in j is less than
                A(i)
"""

def longest_increasing_subsequence(array):
	lis = [[] for i in xrange(len(array))]
	lis[0].append(array[0])
    
	for i in xrange(1, len(array)):
		for j in xrange(i):
			if array[i] > array[j] and len(lis[i]) < len(lis[j]):
				lis[i] = list(lis[j])

		lis[i].append(array[i])

	longest_subseq = lis[0]
	for subseq in lis:
		if len(longest_subseq) < len(subseq):
			longest_subseq = list(subseq)

	return longest_subseq

if __name__ == '__main__':
	array = [3,2,6,4,5,6,7]
	print longest_increasing_subsequence(array) 

