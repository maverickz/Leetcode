def break_words(S, word_list):
    T = [-1]*(len(S)+1)
    T[0] = 0

    for i in xrange(len(S)):
        if T[i] < 0:
            continue

        for word in word_list:
            word_len = len(word)
            end = i + word_len

            if end > len(S):
                continue

            if T[end] > 0:
                continue

            if S[i:end] == word:
                print word, "matched"
                T[end] = i

    print T, len(S), len(T)

    prev = len(S)
    i = T[len(S)]
    print i, prev, S[i:prev]

    while i > 0:
        prev = i
        i = T[i]
        print i, prev, S[i:prev]


    return T[len(S)]

S = "programcreek"
word_list = ["programcree","program","creek"]




print break_words(S, word_list), S[7:]

