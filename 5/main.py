from ast import literal_eval


MAX_PARAMS = 3


def get_data():
    with open('input.txt', 'r') as data:
        return list(literal_eval(data.read()))


def _parse_command(command):
    opcode = command % 100
    command //= 100
    modi = []
    for i in range(MAX_PARAMS):
        modi.append(command % 10)
        command //= 10
    return opcode, tuple(modi)


def execute(data):
    pc = 0
    while True:
        opcode, modi = _parse_command(data[pc])
        pc += 1
        if opcode == 1:
            p1, p2, p3 = data[pc:pc+3]
            v1 = p1 if modi[0] != 0 else data[p1]
            v2 = p2 if modi[1] != 0 else data[p2]
            data[p3] = v1 + v2
            pc += 3
        elif opcode == 2:
            p1, p2, p3 = data[pc:pc+3]
            v1 = p1 if modi[0] != 0 else data[p1]
            v2 = p2 if modi[1] != 0 else data[p2]
            data[p3] = v1 * v2
            pc += 3
        elif opcode == 3:
            addr = data[pc]
            v = input(">>> ")
            data[addr] = int(v)
            pc += 1
        elif opcode == 4:
            p1 = data[pc]
            v1 = p1 if modi[0] != 0 else data[p1]
            print(f"Diagnostic code: {v1}")
            pc += 1
        elif opcode == 5:
            p1, p2 = data[pc:pc+2]
            v1 = p1 if modi[0] != 0 else data[p1]
            v2 = p2 if modi[1] != 0 else data[p2]
            if v1:
                pc = v2
                continue
            pc += 2
        elif opcode == 6:
            p1, p2 = data[pc:pc+2]
            v1 = p1 if modi[0] != 0 else data[p1]
            v2 = p2 if modi[1] != 0 else data[p2]
            if not v1:
                pc = v2
                continue
            pc += 2
        elif opcode == 7:
            p1, p2, p3 = data[pc:pc+3]
            v1 = p1 if modi[0] != 0 else data[p1]
            v2 = p2 if modi[1] != 0 else data[p2]
            data[p3] = 1 if v1 < v2 else 0
            pc += 3
        elif opcode == 8:
            p1, p2, p3 = data[pc:pc+3]
            v1 = p1 if modi[0] != 0 else data[p1]
            v2 = p2 if modi[1] != 0 else data[p2]
            data[p3] = 1 if v1 == v2 else 0
            pc += 3
        elif opcode == 99:
            break
        else:
            raise ValueError(f"Something went wrong, unknown opcode '{opcode}' found")


def main():
    data = get_data()
    execute(data)

if __name__ == '__main__':
    main()
