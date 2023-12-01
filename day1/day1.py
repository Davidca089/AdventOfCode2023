def fetch_addition(line):
    i = 0
    len_line = len(line)
    while i < len_line:
        if line[i] >= '0' and line[i] <= '9':
            accum = int(line[i])*10
            i = len_line - 1
            while i >= 0:
                if line[i] >= '0' and line[i] <= '9':
                    return accum + int(line[i])
                i -= 1
        i += 1


def main():
    with open("input") as f:
        lines = f.readlines()
        accum = 0
        for line in lines:
            accum += fetch_addition(line)
        return accum


if __name__ == '__main__':
    print(main())
