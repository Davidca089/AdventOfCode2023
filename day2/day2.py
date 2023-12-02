def main():
    with open("input") as f:
        lines = f.readlines()
        accum = 0
        for line in lines:
            line = line.strip()
            separate = line.split(":")
            game_num = int(separate[0][5:])
            sets = separate[1].split(";")
            max_vals = {"red": 12, "blue": 14, "green": 13}
            for set in sets:
                colors = set.split(",")
                works = True
                for color_set in colors:
                    number, color = color_set[1:].split(" ")
                    if int(number) > max_vals[color]:
                        works = False
                        break
                if not works:
                    break

            if works:
                accum += game_num
        return accum


print(main())
