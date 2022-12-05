def parse_input(fpath):
    arrangement = []
    instructions = []
    arrangement_complete = False
    with open(fpath, "r") as f:
        for line in f:
            line = line.split("\n")[0]

            if line == "":
                arrangement_complete = True
                continue
            if arrangement_complete:
                instructions.append(line)
            else:
                arrangement.append(line)
    return arrangement, instructions


def parse_arrangement(arrangement):
    stacks = arrangement[-1]
    stack_nums = [int(x) for x in stacks if x.isnumeric()]
    parsed_arrangement = {x: [] for x in stack_nums}
    for row in arrangement[:-1]:
        for stack_num in stack_nums:
            crate = row[stacks.index(str(stack_num))]
            if crate == " ":
                continue
            parsed_arrangement[stack_num].append(crate)
    return parsed_arrangement


def parse_instructions(instructions):
    parsed_instructions = []
    for instruction in instructions:
        move, from_to = instruction.split(" from ")
        move = int(move.split("move ")[1])
        from_, to_ = from_to.split(" to ")
        parsed_instructions.append((move, int(from_), int(to_)))
    return parsed_instructions


def move_one(arrangement, from_stack, to_stack):
    crate = arrangement[from_stack].pop(0)
    arrangement[to_stack] = [crate] + arrangement[to_stack]
    return arrangement


def execute_instruction(arrangement, instruction):
    num_moves, from_stack, to_stack = instruction
    for i in range(num_moves):
        arrangement = move_one(arrangement, from_stack, to_stack)
    return arrangement


def problem_1(fpath):
    arrangement, instructions = parse_input(fpath)
    arrangement = parse_arrangement(arrangement)
    instructions = parse_instructions(instructions)
    for instruction in instructions:
        arrangement = execute_instruction(arrangement, instruction)
    num_stacks = len(arrangement)
    final_str = ""
    for i in range(num_stacks):
        final_str += arrangement[i + 1][0]
    return final_str


def move_many(arrangement, instruction):
    num_moves, from_stack, to_stack = instruction
    crates = arrangement[from_stack][:num_moves]
    arrangement[from_stack] = arrangement[from_stack][num_moves:]
    arrangement[to_stack] = crates + arrangement[to_stack]
    return arrangement


def problem_2(fpath):
    arrangement, instructions = parse_input(fpath)
    arrangement = parse_arrangement(arrangement)
    instructions = parse_instructions(instructions)
    for instruction in instructions:
        arrangement = move_many(arrangement, instruction)
    num_stacks = len(arrangement)
    final_str = ""
    for i in range(num_stacks):
        final_str += arrangement[i + 1][0]
    return final_str

if __name__ == "__main__":
    fpath = "input.txt"
    print(problem_1(fpath))
    print(problem_2(fpath))

