"""
	Given a collection of intervals, merge all overlapping intervals.

	For example:
	Given [1,3],[2,6],[8,10],[15,18],
	return [1,6],[8,10],[15,18]
"""

class Interval:
	def __init__(self,start,end):
		self.start = start
		self.end = end

	def __repr__(self):
		return repr((self.start, self.end))


def merge_intervals(intervals):
	intervals = sorted(intervals, key=lambda interval:interval.start)

	result = []
	result.append(intervals[0])

	for i in xrange(1,len(intervals)):
	    top_interval = result[-1]
	    curr_interval = intervals[i]

	    if top_interval.end >= curr_interval.start:
	        top_interval.end = max(top_interval.end, curr_interval.end)
	    else:
	        result.append(curr_interval)

	return result

if __name__ == '__main__':
	intervals = [Interval(1,3),Interval(15,18),Interval(8,10),Interval(2,6)]
	print merge_intervals(intervals)


    
    
    
    