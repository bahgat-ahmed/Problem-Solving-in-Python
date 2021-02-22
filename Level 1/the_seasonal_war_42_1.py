# TO BE CONTINUED

import numpy as np

# reading the input file
with open('../input/sample-text-file/text_file_42.txt', 'r') as f:
    text = f.read().split('\n')

# getting images dimensions, and pixels into separate lists
img_dims, img_pixels = list(), list()
dim_flag = True
img_pixel = list()
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

valid_dx = [1, 1, 0, -1, -1, -1, 0, 1]
valid_dy = [0, 1, 1, 1, 0, -1, -1, -1]

def valid(i, j, n):
    return (i >= 0 and j >= 0  and i < n and j < n)

def check_eagle(i, j, n):

    if seen[i][j]:
        return

    seen[i][j] = 1

    for idx in range(8):
        dx = i + valid_dx[idx]
        dy = j + valid_dy[idx]
        if valid(dx, dy, n):
            check_eagle(dx, dy, n)

for idx, img in enumerate(img_pixels):
    num_eagles = 0
    img_dim = int(img_dims[idx])
    seen = np.zeros((img_dim, img_dim))
    for i in range(img_dim):
        for j in range(img_dim):
            if img[i][j] == 1:
                check_eagle(i, j, img_dim)
                num_eagles += 1
