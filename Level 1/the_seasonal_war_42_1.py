import numpy as np

def valid(i, j, n):
    return (i >= 0 and j >= 0  and i < n and j < n)

def check_eagle(ii, jj, n):

    seen[ii][jj] = 1

    for idx in range(8):
        dx = ii + valid_dx[idx]
        dy = jj + valid_dy[idx]
        if valid(dx, dy, n) and (seen[dx][dy] == 0) and (int(img[dx][dy]) == 1):

            check_eagle(dx, dy, n)

if __name__ == '__main__':

    # reading the input file
    text_file_name = input()

    with open(text_file_name, 'r') as reader:
        text = reader.read().split('\n')

    # getting images dimensions, and pixels into separate lists
    img_dims, img_pixels = list(), list()
    dim_flag = True
    img_pixel = list()
    for line in text:
        if dim_flag:
            img_dims.append(line)
            if line == '':
                break
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



    output_text = ""

    for idx, img in enumerate(img_pixels):
        num_eagles = 0
        img_dim = int(img_dims[idx])
        seen = np.zeros((img_dim, img_dim))
        for i in range(img_dim):
            for j in range(img_dim):
                if (int(img[i][j]) == 1) and (seen[i][j] == 0):

                    check_eagle(i, j, img_dim)
                    num_eagles += 1

        output_text += f"Image number {idx+1} contains {num_eagles} war eagles.\n"

    with open('output.txt', 'w') as writer:
        text = writer.write(output_text)
