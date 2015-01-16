def find_overlapping_range(pt1, len1, pt2, len2):
    highest_starting_pt = max(pt1, pt2)
    lowest_end_pt = min(pt1+len1, pt2+len2)

    if highest_starting_pt >= lowest_end_pt:
        return None, None
    else:
        overlapping_len = lowest_end_pt - highest_starting_pt
        return highest_starting_pt, overlapping_len


def find_overlapping_rect(rect1, rect2):
    overlapping_rect = {}
    startx, overlapping_width = find_overlapping_range(rect1['x'], rect1['width'], rect2['x'], rect2['width'])
    starty, overlapping_height = find_overlapping_range(rect1['y'], rect1['height'], rect2['y'], rect2['height'])
    if not overlapping_width or not overlapping_height:
        return None
    overlapping_rect['x'] = startx
    overlapping_rect['y'] = starty
    overlapping_rect['width'] = overlapping_width
    overlapping_rect['height'] = overlapping_height
    return overlapping_rect


if __name__ == '__main__':
    # my_rectangle = {

    # # coordinates of bottom-left corner:
    # 'x': 1, 
    # 'y': 5, 

    # # width and height
    # 'width': 10,
    # 'height': 4,

    # }
    rect1 = {'x': 1, 'y': 7, 'width': 10, 'height': 4}
    rect2 = {'x': 9, 'y': 5, 'width': 5, 'height': 4}
    overlapping_rect = find_overlapping_rect(rect1, rect2)
    print overlapping_rect
