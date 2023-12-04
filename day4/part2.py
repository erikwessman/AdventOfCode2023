from collections import defaultdict


def main():
    lines = []
    with open("day4/input.txt", "r") as f:
        lines = f.read().splitlines()

    cards = defaultdict(lambda: 0)

    for i, line in enumerate(lines):
        cards[i + 1] += 1

        _, numbers = line.split(":")

        winning_numbers, my_numbers = numbers.split("|")

        winning_numbers = winning_numbers.strip().split(" ")
        my_numbers = my_numbers.strip().split(" ")

        winning_numbers = {num for num in winning_numbers if num}
        my_numbers = {num for num in my_numbers if num}

        wins = winning_numbers.intersection(my_numbers)

        nr_copies = cards[i + 1]

        for j in range(len(wins)):
            cards[j + i + 2] += 1 * nr_copies

    return sum(cards.values())


if __name__ == "__main__":
    print(main())
