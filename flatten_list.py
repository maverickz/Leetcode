def flatten_list(l):
    output = []
    for elem in l:
        if isinstance(elem, list):
            output += flatten_list(elem)
        else:
            output.append(elem)
    return output

sample = [1,2,[3,4],5,[6,[7,8],9]]
print flatten_list(sample)