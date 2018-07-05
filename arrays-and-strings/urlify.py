import unittest

def urlify(string, length):
    new_str = string.split()
    return '%20'.join(new_str)

class Test(unittest.TestCase):
    '''Test Cases'''

    data = [
        (('much ado about nothing      '), 22,
         ('much%20ado%20about%20nothing')),
        (('Mr John Smith    '), 13, ('Mr%20John%20Smith'))]

    def test_urlify(self):
        for [test_string, length, expected] in self.data:
            actual = urlify(test_string, length)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()