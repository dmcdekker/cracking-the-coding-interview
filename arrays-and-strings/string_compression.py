import unittest

from collections import Counter

def string_compression(string):
    '''Perform basic string compression using counts of repeated characters'''
    result = []
    count = 0
    # iterate through string and add letter + count to result
    for idx in range(len(string)
        ):
        # if letters not the same
        if idx != 0 and (string[idx] != string[idx-1]):
            result.append(string[idx - 1])
            result.append(str(count))
            # reset count variable
            count = 0
        # if the same: increment count
        count += 1
    # add the last element and count
    result.append(string[-1])
    result.append(str(count))

    # if all unique letters: return string
    if len(result) > len(string):
        return string
    
    return ''.join(result)


class Test(unittest.TestCase):
    '''Test Cases'''

    data = [
            ('aaaabbbcccc', 'a4b3c4'),
            ('abcdef', 'abcdef'),
            ('addddbbccc', 'a1d4b2c3')
            ]

    def test_string_compression(self):
        for [test_string, expected] in self.data:
            actual = string_compression(test_string)
            self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()