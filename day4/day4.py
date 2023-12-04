def main():
    with open("input") as f:
        lines = f.read().splitlines()
        accum = 0

        for line in lines:
            line_accum = 0
            # grab both lists of numbers
            splitter = line.split('|')
            winning = [int(num) for num in splitter[0].split(':')[1].split()]
            has = [int(num) for num in splitter[1].split()]

            in_winning = [0] * 100
            for i in winning:
                in_winning[i] = 1

            for i in has:
                if in_winning[i] == 0:
                    continue

                if line_accum == 0:
                    line_accum = 1
                else:
                    line_accum *= 2

            accum += line_accum
        return accum

print(main())
