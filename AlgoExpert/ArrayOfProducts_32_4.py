# O(n) time | O(n) space - where n is the length of the input array
def arrayOfProducts(array):
    array_of_products = [1] * len(array)
	
	prev_num = 1
	for i in range(len(array)):
		array_of_products[i] = prev_num
		prev_num *= array[i]
	
	prev_num = 1
	for i in reversed(range(len(array))):
		array_of_products[i] *= prev_num
		prev_num *= array[i]
	
	return array_of_products
