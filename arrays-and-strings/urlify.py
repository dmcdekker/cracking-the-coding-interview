import unittest

def urlify(string, length):
    new_str = string.split()
    return '%20'.join(new_str)

class Test(unittest.TestCase):
    '''Test Cases'''

    data = [
        (('this is my testy test      '), 29,
         ('this%20is%20my%20testy%20test')),
        (('Ms Jenn Black    '), 13, ('Ms%20Jenn%20Black'))]

    def test_urlify(self):
        for [test_string, length, expected] in self.data:
            actual = urlify(test_string, length)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()