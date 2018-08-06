import unittest

from collections import Counter

def check_permutation(str1, str2):
    '''Check if strings are permutations of each other'''
    # use dictionary
    # runtime = O(n)
    if len(str1) != len(str2):
        return False 

    # use counter to add count for each letter
    counter = Counter()
    for letter in str1:
        counter[letter] += 1
    for letter in str2:
        if counter[letter] == 0:
            return False
        counter[letter] -= 1
    return True

    # shorter counter: just return this line:
    # return Counter(str1) == Counter(str2)

    # sort and compare
    # Runtime = O(n)
    
    # using Python built-in methods:
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
        ('denisee', 'denise')
    )

    def test_permutation(self):
        # true check
        for test_strings in self.test1:
            result = check_permutation(*test_strings)
            self.assertTrue(result)
        # false check
        for test_strings in self.test2:
            result = check_permutation(*test_strings)
            self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()