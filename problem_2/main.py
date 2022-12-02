scores = {"A": 1, "B": 2, "C": 3}

win = {"A": "C", "B": "A", "C": "B"}

conversions = {"X": "A", "Y": "B", "Z": "C"}

result_scores = {"LOSS": 0, "DRAW": 3, "WIN": 6}


def result(opp, me):
    if opp == me:
        return "DRAW"
    elif win[opp] == me:
        return "LOSS"
    else:
        return "WIN"


def solution_part_1(fpath):
    s = []
    with open(fpath, "r") as f:
        for line in f:
            opp, me = line.split("\n")[0].split(" ")
            me = conversions[me]
            res = result(opp, me)
            round_score = scores[me] + result_scores[res]
            s.append(round_score)

    return sum(s)


lose = {val: key for key, val in win.items()}

required_result = {"X": "LOSS", "Y": "DRAW", "Z": "WIN"}


def move_to_take(opp, me):
    required = required_result[me]
    if required == "DRAW":
        return opp
    elif required == "WIN":
        return lose[opp]
    else:
        return win[opp]


def solution_part_2(fpath):
    s = []
    with open(fpath, "r") as f:
        for line in f:
            opp, me = line.split("\n")[0].split(" ")
            move = move_to_take(opp, me)
            round_score = scores[move] + result_scores[required_result[me]]
            s.append(round_score)
    return sum(s)


if __name__ == "__main__":
    fpath = "input.txt"
    print(solution_part_1(fpath))
    print(solution_part_2(fpath))
