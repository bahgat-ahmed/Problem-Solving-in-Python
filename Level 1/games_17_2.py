num_teams = int(input())

host_uniforms, guests_uniforms = list(), list()

host_in_guest_uniform_num = 0

for i in range(num_teams):
    input_uniforms = tuple(map(int, input().split()))

    host_uniforms.append(input_uniforms[0])
    guests_uniforms.append(input_uniforms[1])

for host_uniform in host_uniforms:
    if host_uniform in guests_uniforms:
        # adding the number of times the current host uniform is found in the guest uniforms
        host_in_guest_uniform_num += guests_uniforms.count(host_uniform)

print(host_in_guest_uniform_num)
