def main():
    lines = []
    with open("day4/input.txt", "r") as f:
        lines = f.read().splitlines()

    points = []

    for line in lines:
        _, numbers = line.split(":")

        winning_numbers, my_numbers = numbers.split("|")

        winning_numbers = winning_numbers.strip().split(" ")
        my_numbers = my_numbers.strip().split(" ")

        winning_numbers = {num for num in winning_numbers if num}
        my_numbers = {num for num in my_numbers if num}

        wins = winning_numbers.intersection(my_numbers)

        if len(wins) > 0:
            points.append(pow(2, len(wins) - 1))

    return sum(points)


if __name__ == "__main__":
    print(main())
