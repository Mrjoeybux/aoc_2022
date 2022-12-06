def parse_input(fpath):
    with open(fpath, "r") as f:
        return f.readline().split("\n")[0]


def detect_marker_index(datastream, k=4):
    i = 0
    N = len(datastream) - k
    while i < N:
        if len(set(datastream[i : i + k])) == k:
            return i + k
        i += 1


if __name__ == "__main__":
    fpath = "input.txt"
    txt = parse_input(fpath)
    index = detect_marker_index(txt, k=4)
    print(index)
    index = detect_marker_index(txt, k=14)
    print(index)