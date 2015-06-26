def path_sum(node, path, curr_max):
    path.append(node.val)
    if not node.children:
        curr_max = max(sum(path, curr_max))
        path.pop(-1)
        return curr_max
    else:
        for child in node.children:
            curr_max = path_sum(children, path, curr_max)

    return curr_max

def max_sum(root):
    path = []
    path_sum(root, path, root.val)   