class Node():
    def __init__(self, value):
        self.value = 1
        self.right = None
        self.upper_right = None
        self.up = None
        self.upper_left = None
        self.left = None
        self.down_left = None
        self.down = None
        self.down_right = None

# reading the input file
with open('file_name.txt', 'r') as f:
    text = f.read().split('\n')

# getting images dimensions, and pixels into separate lists
img_dims, img_pixels = list(), list()
dim_flag = True
for line in text:
    if dim_flag:
        img_dims.append(line)
        stop_after = int(line)
        counter = 0
        dim_flag = False
    else:
        img_pixel.append(line)
        counter += 1
        if counter == stop_after:
            img_pixels.append(img_pixel)
            img_pixel = list()
            dim_flag = True

for idx, img in enumerate(img_pixels):
    num_eagles = 0
    for i in range(img_dims[idx]):
        for j in range(img_dims[idx]):
            if img[i][j] == 1: # TO BE CONTINUED
