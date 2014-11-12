def find_longest_unique_substr(string):
    curr_len = 0
    start = 0
    hash_map = {}
    i = 0
    while i < len(string):
        char = string[i]
        if char not in hash_map:
            hash_map[char] = i
        else:
            curr_len = max(curr_len, len(hash_map))
            i = hash_map[char]
            start = i
            hash_map = {}
        i += 1

    return string[start:start+curr_len]


if __name__ == '__main__':
    string = "abcda"
    print find_longest_unique_substr(string)
