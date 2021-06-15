# O(n) time | O(k) space - where n is the number of competitions and k is the
# number of teams
from collections import defaultdict
HOME_TEAM_WON = 1


def tournamentWinner(competitions, results):
    team_points = defaultdict(int)

    for competition, result in zip(competitions, results):
        if result == HOME_TEAM_WON:
            team_points[competition[0]] += 3
        else:
            team_points[competition[1]] += 3
    # get the key (name) of the team that has the maximum value (score)
    winner = max(team_points, key=team_points.get)

    return winner
