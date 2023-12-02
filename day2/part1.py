import re


def main():
    lines = []
    with open("day2/input.txt", "r") as f:
        lines = f.read().splitlines()

    colors_limit = {"red": 12, "blue": 14, "green": 13}
    possible_ids = []

    for line in lines:
        id_str, games_str = line.split(":")

        possible = True

        game_id = int(id_str.split(" ")[1])
        games = re.split(r"[,;]", games_str)

        for game in games:
            count, color = game.strip().split(" ")

            if colors_limit[color] < int(count):
                possible = False
                break

        if possible:
            possible_ids.append(game_id)

    return sum(possible_ids)


if __name__ == "__main__":
    print(main())
