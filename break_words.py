"""
    Given a string s and a dictionary of words dict, determine if s can be 
    segmented into a space-separated sequence of one or more dictionary words.

    For example, given
    s = "leetcode",
    dict = ["leet", "code"].

    Return true because "leetcode" can be segmented as "leet code".

    Let T(i) be denote that the string ending in index 'i' can be split 
    into valid dictionary words and holds the starting index of the last
    valid word that it can be decomposed of
    Boundary condition: T(0) = 0 => string[0:0] can be decomposed into
    valid dictionary word, assuming an empty string is a valid dictionary
    word
"""

def break_words(S, word_list):
    T = [-1]*(len(S)+1)
    T[0] = 0

    for i in xrange(len(S)):
        if T[i] < 0:
            continue

        for word in word_list:
            start = i
            word_len = len(word)
            end = i + word_len

            if end > len(S):
                continue

            # if T[end] > 0:
            #     continue

            if S[start:end] == word:
                print word, "matched"
                T[end] = start

    print T, len(S), len(T)

    end = len(S)
    start = T[end]
    print start, end, S[start:end]

    while start > 0:
        end = start
        start = T[end]
        print start, end, S[start:end]

    return T[len(S)]

S = "programcreek"
word_list = ["programcree","program","creek"]
break_words(S, word_list), S[7:]

