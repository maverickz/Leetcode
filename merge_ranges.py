def merge_ranges(ranges):
    pass
    stack = []
    sorted_ranges = ranges.sort()
    sorted_ranges = sorted(ranges, key=lambda tup: tup[0])
    for interval in sorted_ranges:
        if not stack:
            stack.append(interval)
        else:
            top = stack[-1]
            if top[1] >= interval[0]:
                stack.pop()
                new_interval = top[0], max(top[1], interval[1])
                stack.append(new_interval)
            else:
                stack.append(interval)
    print stack



if __name__ == '__main__':
    merge_ranges(  [(1, 10), (2, 6), (3, 5), (7,9)])