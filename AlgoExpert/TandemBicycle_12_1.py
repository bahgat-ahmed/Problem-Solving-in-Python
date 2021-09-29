# O(log(n)) time | O(1) space - where n is the number of tandem bicycles
def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
    redShirtSpeeds.sort()

	if fastest:
		blueShirtSpeeds.sort(reverse=True)
	else:
		blueShirtSpeeds.sort()
	
	total_speed = 0
	
	for red_speed, blue_speed in zip(redShirtSpeeds, blueShirtSpeeds):
		total_speed += max(red_speed, blue_speed)
			
    return total_speed
