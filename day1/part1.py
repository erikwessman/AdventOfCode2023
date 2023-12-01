def main():
    lines = []
    with open("day1/input.txt", "r") as f:
        lines = f.read().splitlines()

    values = []
    for line in lines:
        l = r = ""
        i = 0

        while i < len(line):
            if not l and line[i].isdigit():
                l = line[i]

            r_i = len(line) - (i + 1)
            if not r and line[r_i].isdigit():
                r = line[r_i]

            if l and r:
                values.append(int(l + r))
                break

            i += 1

    return sum(values)


if __name__ == "__main__":
    print(main())
