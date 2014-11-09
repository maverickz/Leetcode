def permute_string(prefix, suffix):
    if not len(suffix):
        print prefix
    else:
        for i in xrange(len(suffix)):
            permute_string(prefix+suffix[i], suffix[0:i]+suffix[i+1:])


if __name__ == '__main__':
    permute_string('','abc')