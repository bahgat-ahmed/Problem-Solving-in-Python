# O(log(n)) time | O(1) space - where n is the number of tandem bicycles
def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
    redShirtSpeeds.sort()
	blueShirtSpeeds.sort()
	
	if fastest:
		reverse_array_in_place(blueShirtSpeeds)

	total_speed = 0
	
	for red_speed, blue_speed in zip(redShirtSpeeds, blueShirtSpeeds):
		total_speed += max(red_speed, blue_speed)
			
    return total_speed

def reverse_array_in_place(array):
	start = 0
	end = len(array) - 1
	while start < end:
		array[start], array[end] = array[end], array[start]
		start += 1
		end -= 1