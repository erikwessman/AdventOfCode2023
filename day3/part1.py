def main():
    lines = []
    with open("day3/input.txt", "r") as f:
        lines = f.read().splitlines()

    result = 0
    width = len(lines[0])
    height = len(lines)
    visited = set()

    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char == "." or char.isdigit():
                continue

            neighbors = (
                (-1, -1),
                (0, -1),
                (1, -1),
                (-1, 0),
                (1, 0),
                (-1, 1),
                (0, 1),
                (1, 1),
            )

            for n in neighbors:
                n_x = x + n[0]
                n_y = y + n[1]

                if (n_x, n_y) in visited:
                    continue

                if n_x < 0 or n_x > width or n_y < 0 or n_y > height:
                    continue

                visited.add((n_x, n_y))

                if lines[n_y][n_x].isdigit():
                    digit_string = lines[n_y][n_x]

                    # construct left
                    i = n_x - 1
                    while i >= 0 and lines[n_y][i].isdigit():
                        digit_string = lines[n_y][i] + digit_string
                        visited.add((i, n_y))
                        i -= 1

                    # construct right
                    i = n_x + 1
                    while i < width and lines[n_y][i].isdigit():
                        digit_string = digit_string + lines[n_y][i]
                        visited.add((i, n_y))
                        i += 1

                    result += int(digit_string)

    return result


if __name__ == "__main__":
    print(main())
