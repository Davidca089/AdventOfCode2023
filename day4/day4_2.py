def main():
    with open("input") as f:
        lines = f.read().splitlines()
        l = len(lines)
        card_col = [1] * l
        i = 0
        while i < l:
            line = lines[i]
            nb_copies = 0

            # grab both lists of numbers
            splitter = line.split('|')
            winning = [int(num) for num in splitter[0].split(':')[1].split()]
            has = [int(num) for num in splitter[1].split()]

            in_winning = [0] * 100
            for k in winning:
                in_winning[k] += 1
            for k in has:
                if in_winning[k] != 0:
                    nb_copies += 1

            # increase number of cards by the amount of the card im holding
            for k in range(i + 1, i + nb_copies + 1):
                if k >= l:
                    break
                card_col[k] += card_col[i]

            i+= 1

        return sum(card_col)

print(main())
