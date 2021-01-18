num_teams = int(input())

team_uniforms = [tuple(map(int, input().split())) for i in range(num_teams)]

host_in_guest_uniform_num = 0

for host in range(num_teams):
    for guest in range(num_teams):

        if host != guest:
            if team_uniforms[host][0] == team_uniforms[guest][1]:
                host_in_guest_uniform_num += 1

print(host_in_guest_uniform_num)
