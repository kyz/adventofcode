import re, collections

class Node(object):
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        self.children = []

def parse_nodes(f):
    nodes = dict()
    p = re.compile(r"^([a-z]+)\s+\((\d+)\)(?:\s+->\s+([a-z, ]+))?")
    for line in f:
        name, size, kids = p.match(line).groups()
        nodes[name] = Node(name, int(size))
        if kids is not None: nodes[name].children = kids.split(", ")
    return nodes

def build_tree(nodes):
    known_children = set()
    for node in nodes.values():
        known_children |= set(node.children)
        node.children = [nodes[name] for name in node.children]
    return nodes[list(set(nodes.keys()) - known_children)[0]]

def weight(n):
    return n.weight + sum([weight(c) for c in n.children])

def weight_ok(node):
    weights = dict([(n, weight(n)) for n in node.children])
    c = collections.Counter(weights.values())
    if len(c) == 2:
        normal_weight = c.most_common()[0][0]
        odd_weight =  c.most_common()[1][0]
        odd_node = [n for n in node.children if weights[n] == odd_weight][0]
        if weight_ok(odd_node):
            diff = normal_weight - odd_weight
            print("2017 day 7 part 2: %d" % (odd_node.weight + diff))
        return False
    else:
        return True

with open("day07.txt") as f:
    tree = build_tree(parse_nodes(f))
    print("2017 day 7 part 1: %s" % tree.name)
    weight_ok(tree)
