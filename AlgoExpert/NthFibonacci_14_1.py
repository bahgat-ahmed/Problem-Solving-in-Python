# recursive solution
# O (2^n) time | O(n) space - where n is the input number
def getNthFib(n):
    if n < 3:
	return n - 1
    else:
	return getNthFib(n-1) + getNthFib(n-2)
