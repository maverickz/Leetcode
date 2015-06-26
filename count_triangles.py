def count_triangles(segments):
    segments = sorted(segments)
    l = len(segments)
    output = []
    for i in xrange(l-1):
        k = i+2
        for j in xrange(l):
            if k < l and segments[i] + segments[j] > segments[k]:
                output.append((segments[i], segments[j], segments[k]))
                k += 1

    print output

segments = [4, 6, 3, 7]
count_triangles(segments)
