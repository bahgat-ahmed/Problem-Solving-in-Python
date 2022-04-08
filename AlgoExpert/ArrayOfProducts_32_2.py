# O(n) time | O(n) space - where n is the length of the input array
def arrayOfProducts(array):
    left_pos_array = [1] * len(array)
	right_pos_array = [1] * len(array)
	
	left_running_product = 1
	for i in range(len(array)):
		left_pos_array[i] = left_running_product
		left_running_product *= array[i]
	
	right_running_product = 1
	for i in reversed(range(len(array))):
		right_pos_array[i] = right_running_product
		right_running_product *= array[i]
		
	array_of_products = []
	for i in range(len(array)):
		array_of_products.append(left_pos_array[i] * right_pos_array[i])
	
	return array_of_products
