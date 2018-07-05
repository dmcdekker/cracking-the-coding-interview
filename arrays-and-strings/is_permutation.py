import unittest

def is_permutation(str1, str2):
    '''Check if strings are permutations of each other'''
    # use dictionary
    # runtime = O(n)
    if len(str1) != len(str2):
        return False 

    str1_dict = {}

    for letter in str1:
        str1_dict[letter] = str1_dict.get(letter, 0) + 1
    for letter in str2:
        if letter not in str1_dict:
            return False    

    return True

    # sort and compare
    # Runtime = O(n)
    # return sorted(str1) == sorted(str2)


class Test(unittest.TestCase):
    '''Test Cases'''
    test1 = (
        ('abcd', 'bacd'),
        ('123456', '564312'),
        ('denise', 'nidese'),
    )
    test2 = (
        ('abcd', 'bacd2'),
        ('4567', '8910'),
        ('denise', 'den5hw'),
    )

    def test_permutation(self):
        # true check
        for test_strings in self.test1:
            result = is_permutation(*test_strings)
            self.assertTrue(result)
        # false check
        for test_strings in self.test2:
            result = is_permutation(*test_strings)
            self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()