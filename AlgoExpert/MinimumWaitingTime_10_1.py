# O(nlogn) time | O(1) space - where n is the number of queries 
def minimumWaitingTime(queries):
	
	queries.sort()
	
	total_waiting = 0
	for idx, query in enumerate(queries[:-1]):
		total_waiting += sum(queries[:idx + 1])
		
    return total_waiting


