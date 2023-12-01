def main():
    lines = []
    with open("day1/input.txt", "r") as f:
        lines = f.read().splitlines()

    digits = ("one", "two", "three", "four", "five", "six", "seven", "eight", "nine")
    digits_map = {digit: value + 1 for value, digit in enumerate(digits)}
    digits_lengths = {len(digit) for digit in digits}

    values = []
    for line in lines:
        l = r = 0
        i = 0

        while i < len(line):

            if not l:
                if line[i].isdigit():
                    l = int(line[i])
                else:
                    for d_l in digits_lengths:
                        word = line[i : i + d_l]
                        if word in digits_map:
                            l = digits_map[word]
                            break

            r_i = len(line) - (i + 1)
            if not r:
                if line[r_i].isdigit():
                    r = int(line[r_i])
                else:
                    for d_l in digits_lengths:
                        word = line[r_i - (d_l - 1) : r_i + 1]
                        if word in digits_map:
                            r = digits_map[word]
                            break

            if l and r:
                values.append(int(str(l) + str(r)))
                break

            i += 1

    return sum(values)


if __name__ == "__main__":
    print(main())
