def get_attr_number(node):
    return sum(len(child.attrib) for child in node.iter())
