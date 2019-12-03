def get_fuel_cost(mass):
    return (mass // 3) - 2


def get_fuel_cost_recursive(mass):
    base_cost = get_fuel_cost(mass)
    if base_cost <= 0:
        return 0
    return base_cost + get_fuel_cost_recursive(base_cost)


def get_raw_data():
    with open('part1.txt', 'r') as data:
        data = data.read().split()
    return data


def exercise(data, mode=0):
    f = get_fuel_cost if not mode else get_fuel_cost_recursive
    return sum(f(int(m)) for m in data)


def main():
    data = get_raw_data()
    p1 = exercise(data)
    p2 = exercise(data, 1)

    print(f"Result part 1: {p1}\nResult part 2: {p2}")

if __name__ == '__main__':
    main()
