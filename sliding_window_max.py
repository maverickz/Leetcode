def sliding_window_max(array, window_size):
    if len(array) < window_size:
        return 
    w = window_size
    queue = []
    front = 0
    back = -1

    for i in xrange(window_size):
        while queue and array[i] >= array[queue[back]]:
            queue.pop()
        queue.append(i)

    for i in xrange(window_size, len(array)):
        print array[queue[front]]
        while queue and queue[front] <= i - window_size:
            queue.pop(front)

        while queue and array[i] > array[queue[back]]:
            queue.pop()
        queue.append(i)
    print array[queue[front]]

sliding_window_max([8, 5, 10, 7, 9, 4, 15, 12, 90, 13], 4)

