RANGE = range(234208, 765869)


def check_value(value, part2=False):
    cur = prev = value
    double = ordered = False
    count = 0
    while value:
        cur = value % 10
        if not double:
            if cur == prev:
                if not part2:
                    double = True
                count += 1
            elif count == 1:
                double = True
            else:
                count = 0
        if cur <=prev:
            ordered = True
        else:
            ordered = False
            break
        # updates
        prev = cur
        value //= 10
    if not double and part2 and count == 1:
        double = True
    return double and ordered


def get_candidates(part2=False):
    candidates = []
    for value in RANGE:
        if check_value(value, part2=part2):
            candidates.append(value)
    return candidates


def main():
    candidates = get_candidates()
    candidates2 = get_candidates(True)
    print(f"Part 1: {len(candidates)}")
    print(f"Part 2: {len(candidates2)}")


if __name__ == '__main__':
    main()
