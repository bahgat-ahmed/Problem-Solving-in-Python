# O(n^2) time | O(n) space - where n is the length of the input array
def arrayOfProducts(array):
    product_array = []
	for i in range(len(array)):
		product_array.append(get_product(i, array))
	return product_array

		
def get_product(i, array):
	product = 1
	for idx in range(len(array)):
		if idx != i:
			product *= array[idx]
	return product
