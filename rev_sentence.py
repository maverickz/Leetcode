def reverse(string, start, end):
    while start < end:
        string[start], string[end] = string[end], string[start]
        start += 1
        end -= 1

def rev_sentence(sentence):
    sentence = list(sentence[::-1])
    i = 0
    N = len(sentence)
    start = 0
    for i in xrange(N):
        if sentence[i] == ' ':
            reverse(sentence, start, i-1)
            start = i+1
        if i == N-1:
            reverse(sentence, start, i)

    return ''.join(sentence)

if __name__ == '__main__':
    input_sentence = "Write efficient algorithms haven't made me rich"
    assert input_sentence == rev_sentence(rev_sentence(input_sentence))


