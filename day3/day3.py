def check_neighbourhood(start, end, string, line_num, max_line_num,end_of_line):
    if start != 0:
        if string[line_num][start-1] != '.':
            return True

    while start < end:
        for i in range(-1,2):
            if line_num == 0 or start + i < 0 or start + i >= end_of_line:
                continue
            #valid
            if string[line_num-1][start+i] != '.' and not string[line_num-1][start+i].isdigit():
                return True

        for i in range(-1,2):
            if line_num == max_line_num-1 or start + i < 0 or start + i >= end_of_line:
                continue
            #valid
            if string[line_num+1][start+i] != '.' and not string[line_num+1][start+i].isdigit():
                return True

        start += 1

    if end != end_of_line:
        if string[line_num][end] != '.':
            return True

    return False

def main():
    with open("input") as f:
        lines = f.read().splitlines()
        i = 0
        l = len(lines)
        accum = 0
        while i < l:
            it = 0
            l_len = len(lines[i])
            while it < l_len:
                # Grab the first digit found
                j = it
                while j < l_len and not lines[i][j].isdigit():
                    j+=1

                if j == l_len and not lines[i][j-1].isdigit():
                    break

                start = j
                while j < l_len and lines[i][j].isdigit():
                    j += 1
                end = j
                if check_neighbourhood(start, end, lines, i, l,l_len):
                    accum += int(lines[i][start:end])

                it = end

            i+= 1

        return accum

print(main())
