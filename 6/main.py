class Node(object):

    def __init__(self, parent=None):
        self.__parent = parent
        if self.__parent:
            self.__parent.children.append(self)
        self.children = []

    @property
    def parent(self):
        return self.__parent

    @parent.setter
    def parent(self, value):
        self.__parent = value
        value.children.append(self)

    @property
    def neighbors(self):
        if self.parent:
            return self.children + [self.parent]
        return self.children

    def count_parents(self):
        if not self.parent:
            return 0
        return 1 + self.parent.count_parents()


def generate_nodes(input):
    nodes = {}
    for line in input:
        left, right = line.split(')')
        if not left in nodes:
            nodes[left] = Node()
        if right in nodes and not nodes[right].parent:
            nodes[right].parent = nodes[left]
        else:
            nodes[right] = Node(nodes[left])
    return nodes


def count_orbits(nodes):
    return sum([n.count_parents() for n in list(nodes.values())])


def search(start, target, depth=0, checked=[]):
    if target in start.neighbors:
        return depth
    for neighbor in start.neighbors:
        if neighbor not in checked:
            checked.append(start)
            res = search(neighbor, target, depth + 1, checked)
            if res:
                return res


def find_min_orbital_path(nodes):
    return search(nodes['YOU'], nodes['SAN']) - 1


def main():
    with open("input.txt", "r") as f:
        data = f.read().splitlines()
    nodes = generate_nodes(data)
    print(f"Part 1: {count_orbits(nodes)}")
    print(f"Part 2: {find_min_orbital_path(nodes)}")


if __name__ == '__main__':
    main()
