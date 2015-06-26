def sliding_window_max(array, window_size):
    if len(array) < window_size:
        return 
    queue = []
    front = 0
    back = -1

    for i in xrange(window_size):
        while queue and array[i] >= array[queue[back]]:
            print queue
            queue.pop()
        queue.append(i)
        print queue

    for i in xrange(window_size, len(array)):
        print array[queue[front]]
        while queue and queue[front] <= i - window_size:
            print queue
            queue.pop(front)
        print '*'*50
        while queue and array[i] > array[queue[back]]:
            print queue
            queue.pop()
        queue.append(i)
    print array[queue[front]]

sliding_window_max([8, 5, 10, 7, 9, 4, 15, 12, 90, 13], 4)

