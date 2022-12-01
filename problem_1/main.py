def solution(fpath):
    calories = []
    with open(fpath, "r") as f:
        this_elf = 0
        for line in f:
            val = line.split("\n")[0]
            if val == "":
                calories.append(this_elf)
                this_elf = 0
            else:
                this_elf += int(val)

    first = max(calories)
    calories.pop(calories.index(first))

    second = max(calories)
    calories.pop(calories.index(second))

    third = max(calories)
    return first, second, third


if __name__ == "__main__":
    fpath = "input.txt"
    ans = solution(fpath)
    print(ans)
    print(sum(ans))
