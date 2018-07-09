import unittest

def string_compression(string):
    '''Perform basic string compression using counts of repeated characters'''
    string_dict = {}
    compressed = []
    for letter in string:
        string_dict[letter] = string_dict.get(letter, 0) + 1
    for letter, num in string_dict.items():
        compressed.append(letter)
        compressed.append(str(num))
    if len(compressed) > len(string):
        return string    
    return ''.join(compressed) 


class Test(unittest.TestCase):
    '''Test Cases'''

    data = [
            ('aaaabbcccc', 'a4b2c4'),
            ('abcdef', 'abcdef')
            ]

    def test_string_compression(self):
        for [test_string, expected] in self.data:
            actual = string_compression(test_string)
            self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()