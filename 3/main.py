START = (0, 0)


def get_points(commands):
    points = []
    cur_pos = START

    for cmd in commands:
        side = cmd[0]
        length = int(cmd[1:])
        r = range(1, length + 1)

        if side == 'R':
            points += [(cur_pos[0] + x, cur_pos[1]) for x in r]
            cur_pos = (cur_pos[0] + length, cur_pos[1])
        elif side == 'L':
            points += [(cur_pos[0] - x, cur_pos[1]) for x in r]
            cur_pos = (cur_pos[0] - length, cur_pos[1])
        elif side == 'U':
            points += [(cur_pos[0], cur_pos[1] + y) for y in r]
            cur_pos = (cur_pos[0], cur_pos[1] + length)
        elif side == 'D':
            points += [(cur_pos[0], cur_pos[1] - y) for y in r]
            cur_pos = (cur_pos[0], cur_pos[1] - length)
        else:
            raise ValueError("What the fuck?")
    return points


def get_commands():
    with open('part1.txt', 'r') as f:
        data = f.read().split()
    return data[0].split(','), data[1].split(',')


def get_distances(points):
    distances = []
    for point in points:
        distances.append(abs(START[0] - point[0]) + abs(START[1] - point[1]))
    return distances


def get_steps(w1_pts, w2_pts, intersections):
    steps = []

    for intersection in intersections:
        steps.append(w1_pts.index(intersection) + w2_pts.index(intersection) + 2)
    return steps


def main():
    w1_cmd, w2_cmd = get_commands()
    w1_pts = get_points(w1_cmd)
    w2_pts = get_points(w2_cmd)
    intersections = list(set(w1_pts) & set(w2_pts))
    distances = get_distances(intersections)
    print(f"Part 1: {min(distances)}")
    steps = get_steps(w1_pts, w2_pts, intersections)
    print(f"Part 2: {min(steps)}")

if __name__ == '__main__':
    main()
