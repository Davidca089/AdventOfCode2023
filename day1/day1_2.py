def valid_digit_substring(line, start):
    dic = {"one": 1,
           "two": 2,
           "three": 3,
           "four": 4,
           "five": 5,
           "six": 6,
           "seven": 7,
           "eight": 8,
           "nine": 9,
           }

    for key in dic:
        substr = line[start:start + len(key)+1]
        if key in substr:
            return dic[key], True

    return -1, False


def fetch_addition(line):
    i = 0
    len_line = len(line)
    while i < len_line:
        val, happened = valid_digit_substring(line, i)
        if (line[i] >= '0' and line[i] <= '9') or happened:
            if (line[i] >= '0' and line[i] <= '9'):
                val = int(line[i]) * 10
            else:
                val *= 10
            i = len_line - 1
            while i >= 0:
                second_val, happened = valid_digit_substring(line, i-3)
                if (line[i] >= '0' and line[i] <= '9') or happened:
                    if (line[i] >= '0' and line[i] <= '9'):
                        return val + int(line[i])
                    else:
                        return val + second_val
                i -= 1
        i += 1


def main():
    with open("input") as f:
        lines = f.readlines()
        accum = 0
        for line in lines:
            val = fetch_addition(line)
            accum += val
        return accum


if __name__ == '__main__':
    print(main())
