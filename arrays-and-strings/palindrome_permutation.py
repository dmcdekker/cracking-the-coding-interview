import unittest

def palindrome_permutation(string):
    '''Check if string is permutation of a palindrome'''
    count_letters = {}
    for letter in string.lower():
        if letter != ' ':
            count_letters[letter] = count_letters.get(letter, 0) + 1
    count = 0
    for letter, number in count_letters.iteritems():
        if number % 2 != 0:
            count += 1
    return count <= 1


class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ('Tact Coa', True),
        ('jhsabckuj ahjsbckj', True),
        ('Able was I ere I saw Elba', True),
        ('So patient a nurse to nurse a patient so', False),
        ('Random Words', False),
        ('Not a Palindrome', False),
        ('no x in nixon', True),
        ('azAZ', True)]

    def test_pal_perm(self):
        for [test_string, expected] in self.data:
            actual = palindrome_permutation(test_string)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()   
