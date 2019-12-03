from ast import literal_eval


def get_data():
    with open('part1.txt', 'r') as data:
        return list(literal_eval(data.read()))


def part1(data):
    result = execute(data[:])
    print(f"Part 1: {result}")


def part2(data):
    EXPECTED = 19690720
    for noun in range(100):
        for verb in range(100):
            res = execute(data[:], noun, verb)
            if res == EXPECTED:
                print(f"Part 2: {(100 * noun) + verb}")
                return


def execute(data, noun=12, verb=2):
    data[1] = noun
    data[2] = verb
    i = 0
    while True:
        opcode, v1, v2, r = data[i:i+4]
        if opcode == 1:
            data[r] = data[v1] + data[v2]
        elif opcode == 2:
            data[r] = data[v1] * data[v2]
        elif opcode == 99:
            break
        else:
            raise ValueError("Something went wrong, unknown opcode found")
        i += 4
    return data[0]


def main():
    data = get_data()
    part1(data)
    part2(data)

if __name__ == '__main__':
    main()
