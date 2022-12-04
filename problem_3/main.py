import string


def priority(item):
    position = 1 + string.ascii_lowercase.index(item.lower())
    return position + 26 * int(item.isupper())


def parse_file(fpath):
    rucksacks = []
    with open(fpath, "r") as f:
        for line in f:
            rucksack = line.split("\n")[0]
            n = len(rucksack)
            rucksacks.append((rucksack[: n // 2], rucksack[n // 2 :]))
    return rucksacks


def shared_item(rucksack):
    compartment_1, compartment_2 = rucksack
    intersection = set(compartment_1).intersection(set(compartment_2))
    return next(iter(intersection))


def problem_1(fpath):
    rucksacks = parse_file(fpath)
    shared_items = map(shared_item, rucksacks)
    return sum(map(priority, shared_items))


def get_groups(rucksacks):
    it = iter(rucksacks)
    for rucksack in it:
        yield (rucksack, next(it), next(it))


def compute_badge(group):
    badge = None
    for rucksack in group:
        all_items = rucksack[0] + rucksack[1]
        if badge is None:
            badge = set(all_items)
        else:
            badge = badge.intersection(all_items)
    return next(iter(badge))


def problem_2(fpath):
    rucksacks = parse_file(fpath)
    group_it = get_groups(rucksacks)
    badges = map(compute_badge, group_it)
    return sum(map(priority, badges))


if __name__ == "__main__":
    fpath = "input.txt"
    print(problem_1(fpath))
    print(problem_2(fpath))
