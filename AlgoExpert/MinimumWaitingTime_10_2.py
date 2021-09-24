# O(nlogn) time | O(1) space - where n is the number of queries 
def minimumWaitingTime(queries):
    
	queries.sort()
	
	total_waiting = 0
	for idx, duration in enumerate(queries[:-1]):
		queries_left = len(queries) - (idx + 1)
		total_waiting += duration * queries_left
		
    return total_waiting
	
