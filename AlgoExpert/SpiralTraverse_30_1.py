# O(n) time | O(n) space - where n is the total number of elements in the array
# iterative solution 1
def spiralTraverse(array):
	flattened_spiral = []
	n_rows = len(array)
	n_cols = len(array[0])
	start_row = 0
	start_col = 0
	while start_row <= n_rows - 1 and start_col <= n_cols - 1:
		flattened_spiral.extend(traverse_rectangle(array, start_row, start_col, n_rows, n_cols))
		n_rows -= 1
		n_cols -= 1
		start_row += 1
		start_col += 1
	return flattened_spiral

				
def traverse_rectangle(array, start_row, start_col, n_rows, n_cols):
	traversed_numbers = []
	for i in range(start_row, n_rows):
		if i == start_row:
			for j in range(start_col, n_cols):
				traversed_numbers.append(array[i][j])
		elif i == n_rows - 1:
			for j in reversed(range(start_col, n_cols)):
				traversed_numbers.append(array[i][j])
		else:
			traversed_numbers.append(array[i][n_cols - 1])
	if start_row != n_cols - 1:
		for i in reversed(range(start_row + 1, n_rows - 1)):
			traversed_numbers.append(array[i][start_col])
		
	return traversed_numbers
