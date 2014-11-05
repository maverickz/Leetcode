"""
    Removes duplicate words in a sentence delimited by space
    Returns the array of unique words and a list of indices
    required to reconstruct the original sentence.
    For example: sentece = 'this specification is the specification for a specification'
                 unique_words = ['this', 'specification', 'is', 'the', 'for', 'a']
                 indices = [0, 1, 2, 3, 1, 4, 5, 1]
"""
def remove_duplicates(sentence):
    inp = sentence.split()
    hash_map = {}
    output = []
    index_array = []
    for idx, word in enumerate(inp):
        if word in hash_map:
            index_array.append(hash_map[word])
        else:
            inserted_index = len(output)
            hash_map[word] = inserted_index
            output.append(word)
            index_array.append(inserted_index)        
    return output, index_array

import unittest

class TestCompression(unittest.TestCase):
    def setUp(self):
        pass

    def test_simple_sentence(self):
        sentence =  "this specification is the specification for a specification"
        output, indices = remove_duplicates(sentence)
        constructed_sentence = ''
        for index in indices:
            constructed_sentence += output[index] + ' '
        constructed_sentence = constructed_sentence.rstrip()
        self.assertEqual(sentence, constructed_sentence)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()