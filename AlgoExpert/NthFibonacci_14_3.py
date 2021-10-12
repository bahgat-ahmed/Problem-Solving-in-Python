# iterative solution
# O(n) time | O(1) space - where n is the input number 
def getNthFib(n):
    if n < 3:
	return n - 1
    fib_n_2 = 1
    fib_n_1 = 0
    counter = 3
    while counter <= n:
	current_fib = fib_n_2 + fib_n_1
	fib_n_1 = fib_n_2
	fib_n_2 = current_fib
	counter += 1

    return current_fib
