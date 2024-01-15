def parse_game(line):
    game_num, all_draws = line.split(": ")
    max_r, max_g, max_b = 0, 0, 0
    for draw in all_draws.split("; "):
        for d in draw.split(", "):
            count, colour = d.split(" ")
            if   colour == "red":   max_r = max(max_r, int(count))
            elif colour == "green": max_g = max(max_g, int(count))
            elif colour == "blue":  max_b = max(max_b, int(count))
    return (int(game_num[4:]), max_r, max_g, max_b)

def possible(game):
    return game[1] <= 12 and game[2] <= 13 and game[3] <= 14

def game_power(game):
    return game[1] * game[2] * game[3]

with open("day02.txt", "r") as fh:
    games = [parse_game(line.strip()) for line in fh]
    print("2023 day 02 part 1: %d" % sum(g[0] for g in games if possible(g)))
    print("2023 day 02 part 2: %d" % sum(game_power(g) for g in games))
