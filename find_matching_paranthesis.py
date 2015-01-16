def find_matching_paranthesis(sentence, start):
    if sentence[start] != '(':
        return None
    i = start
    count = 0
    for i in xrange(start, len(sentence)):
        if sentence[i] == '(':
            count += 1
        if sentence[i] == ')':
            count -= 1
        if count == 0:
            return i

    return None


if __name__ == '__main__':
    sentence = "Sometimes (when I nest them (my parentheticals) too much (like this (and this))) they get confusing."
    end = find_matching_paranthesis(sentence, 28)
    print end, sentence[28:end+1]
