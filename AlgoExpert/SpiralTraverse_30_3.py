# O(n) time | O(n) space - where n is the total number of elements in the array
# recursive solution
def spiralTraverse(array):
	flattened_spiral = []
	start_row = 0
	start_col = 0
	n_rows = len(array)
	n_cols = len(array[0])
	
	traverse_rectangle(array, start_row, start_col, n_rows, n_cols, flattened_spiral)

	return flattened_spiral

				
def traverse_rectangle(array, start_row, start_col, n_rows, n_cols, flattened_spiral):
	
	if start_row > n_rows - 1 or start_col > n_cols - 1:
		return
	
	for col in range(start_col, n_cols):
		flattened_spiral.append(array[start_row][col])
		
	for row in range(start_row + 1, n_rows):
		flattened_spiral.append(array[row][n_cols - 1])
		
	for col in reversed(range(start_col, n_cols - 1)):
		# handling the edge case when there's a singe row in the middle
		# of the matrix. In this case, we don't want to double-count the
		# values in this row which we've already counted in the first for
		# loop above.
		if start_row == n_rows - 1:
			break
		flattened_spiral.append(array[n_rows - 1][col])
		
	for row in reversed(range(start_row + 1, n_rows - 1)):
		# handling the edge case when there's a singe column in the middle
		# of the matrix. In this case, we don't want to double-count the
		# values in this column which we've already counted in the second for
		# loop above.
		if start_col == n_cols - 1:
			break
		flattened_spiral.append(array[row][start_col])
		
	traverse_rectangle(array, start_row + 1, start_col + 1, n_rows - 1, n_cols - 1, flattened_spiral)
