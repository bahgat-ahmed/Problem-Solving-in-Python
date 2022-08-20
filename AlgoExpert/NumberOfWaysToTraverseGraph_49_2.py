# O(n * m) time | O(n * m) space - where n is the width of the graph
# and m is its height
def numberOfWaysToTraverseGraph(width, height):
    number_of_ways = [[0] * width for _ in range(height)]
    
    for height_idx in range(height):
        for width_idx in range(width):
            if height_idx == 0 or width_idx == 0:
                number_of_ways[height_idx][width_idx] = 1
            else:
                num_ways_left = number_of_ways[height_idx][width_idx - 1]
                num_ways_up = number_of_ways[height_idx - 1][width_idx]
                number_of_ways[height_idx][width_idx] = num_ways_left + num_ways_up

    return number_of_ways[-1][-1]
    