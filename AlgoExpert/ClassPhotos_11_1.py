# O(n^2) time | O(n) space - where n is the number of students wearing red
# shirts or the number of students wearning blue shirts
def classPhotos(redShirtHeights, blueShirtHeights):
	redShirtHeights_copy = sorted(redShirtHeights)
	blueShirtHeights_copy = sorted(blueShirtHeights)
	
	valid_height_num = 0
	for red_idx, red_height in enumerate(redShirtHeights_copy):
		for blue_idx, blue_height in enumerate(blueShirtHeights_copy):
			if red_height > blue_height:
				valid_height_num += 1
				blueShirtHeights_copy[blue_idx] = float('inf')
				break
				
	if len(redShirtHeights) == valid_height_num:
		return True
	else:
		redShirtHeights_copy = sorted(redShirtHeights)
		blueShirtHeights_copy = sorted(blueShirtHeights)
	
		valid_height_num = 0
		for blue_idx, blue_height in enumerate(blueShirtHeights_copy):
			for red_idx, red_height in enumerate(redShirtHeights_copy):
				if blue_height > red_height:
					valid_height_num += 1
					redShirtHeights_copy[red_idx] = float('inf')
					break
					
		if len(redShirtHeights) == valid_height_num:
			return True
		else:
			return False
