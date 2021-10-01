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
	if len(array) % 2 == 0:
		array_middle = int(len(array)/2)
	else:
		array_middle = int((len(array) - 1 )/2)
	for idx, item in enumerate(array[:array_middle]):
		hold_item = array[-idx-1]
		array[-idx-1] = item
		array[idx] = hold_item