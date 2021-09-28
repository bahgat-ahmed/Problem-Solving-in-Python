# O(log(n)) time | O(1) space - where n is the number of students wearing red
# shirts or the number of students wearning blue shirts
def classPhotos(redShirtHeights, blueShirtHeights):
	# sort in place
	redShirtHeights.sort(reverse=True)
	blueShirtHeights.sort(reverse=True)
	
	if redShirtHeights[0] > blueShirtHeights[0]:
		for idx in range(len(redShirtHeights)):
			if redShirtHeights[idx] <= blueShirtHeights[idx]:
				return False
				
	elif redShirtHeights[0] < blueShirtHeights[0]:
		for idx in range(len(redShirtHeights)):
			if redShirtHeights[idx] >= blueShirtHeights[idx]:
				return False
	else:
		return False
	
	return True
    
	
