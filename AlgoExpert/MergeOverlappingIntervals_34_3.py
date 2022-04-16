# O(n*log(n)) time | O(n) space - where n is the length of the input array
def mergeOverlappingIntervals(intervals):
	sorted_intervals = sorted(intervals, key = lambda x: x[0])
	
	merged_intervals = []
	current_interval = sorted_intervals[0]
	merged_intervals.append(current_interval)
	
    for next_interval in sorted_intervals:
		_, current_interval_end = current_interval
		next_interval_start, next_interval_end = next_interval
		
		if next_interval_start <= current_interval_end:
			current_interval[1] = max(next_interval_end, current_interval_end)
		else:
			current_interval = next_interval
            merged_intervals.append(current_interval)

	return merged_intervals
