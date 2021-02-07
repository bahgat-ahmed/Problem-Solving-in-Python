input_ = lambda: map(int, input().split())

num_forces = int(input())

x_equil, y_equil, z_equil = 0, 0, 0

for i in range(num_forces):
    f_x, f_y, f_z = input_()
    x_equil += f_x
    y_equil += f_y
    z_equil += f_z

if (x_equil == 0) and (y_equil == 0) and (z_equil == 0):
    print("YES")
else:
    print("NO")    
