import json
import re


class Node:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return json.dumps({"val": self.val.__str__(), "left": self.left.__str__(), "right": self.right.__str__()})


def deserialize(data):
    str_data = json.loads(data)
    dump_node = None

    if str_data["val"]:
        dump_node = Node(str_data["val"])
        if str_data["left"]:
            if str_data["left"] != 'None' and re.match(r'^-?\d+(?:\.\d+)?$', str_data["left"]) is None:
                dump_node.left = deserialize(str_data["left"])
            elif re.match(r'^-?\d+(?:\.\d+)?$', str_data["left"]) is not None:
                dump_node.left = float(str_data["left"])
            else:
                dump_node.left = None

        if str_data["right"]:
            if str_data["right"] != 'None' and re.match(r'^-?\d+(?:\.\d+)?$', str_data["right"]) is None:
                dump_node.right = deserialize(str_data["right"])
            elif re.match(r'^-?\d+(?:\.\d+)?$', str_data["right"]) is not None:
                dump_node.right = float(str_data["right"])
            else:
                dump_node.right = None

    return dump_node


def serialize(data):
    return json.dumps({"val": data.val.__str__(), "left": data.left.__str__(), "right": data.right.__str__()})


if __name__ == "__main__":
    node = Node('root', Node('left', Node('left.left')), Node('right'))
    assert deserialize(serialize(node)).left.left.val == 'left.left'
    print('----end----')
