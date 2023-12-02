import re
from functools import reduce
from operator import mul


def main():
    lines = []
    with open("day2/input.txt", "r") as f:
        lines = f.read().splitlines()

    powers = []

    for line in lines:
        _, games_str = line.split(":")

        colors_map = {"red": 0, "blue": 0, "green": 0}
        games = re.split(r"[,;]", games_str)

        for game in games:
            count, color = game.strip().split(" ")
            colors_map[color] = max(colors_map[color], int(count))

        powers.append(reduce(mul, colors_map.values()))

    return sum(powers)


if __name__ == "__main__":
    print(main())
