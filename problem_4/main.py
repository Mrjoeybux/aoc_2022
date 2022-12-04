def parse_file(fpath):
    pairs = []
    with open(fpath, "r") as f:
        for line in f:
            pair = line.split("\n")[0].split(",")
            pairs.append(pair)
    return pairs


def get_range(elf):
    return tuple(map(int, elf.split("-")))


def is_contained(range1, range2):
    sort = list(sorted((range1, range2), key=lambda x: x[0]))
    lower1, upper1 = sort[0]
    lower2, upper2 = sort[1]
    return (lower1 <= lower2) and (upper1 >= upper2)


def problem_1(fpath):
    pairs = parse_file(fpath)
    first, second = zip(*pairs)
    ranges = zip(map(get_range, first), map(get_range, second))
    f = lambda x: is_contained(*x)
    return sum(map(f, ranges))


def overlaps(range1, range2):
    sort = list(sorted((range1, range2), key=lambda x: x[0]))
    upper1 = sort[0][1]
    lower2 = sort[1][0]
    return upper1 >= lower2


def problem_2(fpath):
    pairs = parse_file(fpath)
    first, second = zip(*pairs)
    ranges = zip(map(get_range, first), map(get_range, second))
    f = lambda x: overlaps(*x)
    return sum(map(f, ranges))


if __name__ == "__main__":
    fpath = "input.txt"
    print(problem_1(fpath))
    print(problem_2(fpath))
