# O(n + m) time | O(1) space - where n is the width of the graph
# and m is its height
def numberOfWaysToTraverseGraph(width, height):
    x_distance_to_corner = width - 1
    y_distance_to_corner = height - 1

    # the number of permutations of right and down movements
    # is the number of ways to reach the bottom right corner
    numerator = factorial(x_distance_to_corner + y_distance_to_corner)
    denominator = factorial(x_distance_to_corner) * factorial(y_distance_to_corner)
    
    return numerator // denominator


def factorial(num):
    result = 1
    
    for n in range(2, num + 1):
        result *= n

    return result
