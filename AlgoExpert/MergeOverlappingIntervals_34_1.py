# O(n*log(n)) time | O(n) space - where n is the length of the input array
def mergeOverlappingIntervals(intervals):
	intervals.sort(key = lambda x: x[0])
	merged_intervals = [intervals[0]]
    for i in range(len(intervals) - 1):
		if intervals[i + 1][0] <= merged_intervals[-1][1]:
			if intervals[i + 1][1] > merged_intervals[-1][1]:
				merged_intervals[-1][1] = intervals[i + 1][1]
		else:
            merged_intervals.append(intervals[i + 1])

	return merged_intervals
