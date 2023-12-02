def main():
    with open("input") as f:
        lines = f.readlines()
        accum = 0
        for line in lines:
            line = line.strip()
            separate = line.split(":")
            sets = separate[1].split(";")
            vals = {"red": 0, "blue": 0, "green": 0}
            for set in sets:
                colors = set.split(",")
                for color_set in colors:
                    number, color = color_set[1:].split(" ")
                    if int(number) > vals[color]:
                        vals[color] = int(number)

            accum += vals["red"] * vals["blue"] * vals["green"]
        return accum


print(main())
