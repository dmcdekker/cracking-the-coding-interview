import unittest

    


def urlify_1(string, length):
    '''Write method to replace all spaces in a string with %20.
        May assume there's enough space at the end to hold the
        additional chars and that you are given the true length
        of the string'''
    
    new_index = len(string)

    for idx in reversed(range(length)):
        # if single space
        if string[idx] == ' ':
            # replace spaces
            string[new_index - 3:new_index] = '%20'
            # move end of string
            new_index -= 3
        # else if 
        else:
            # move characters
            string[new_index - 1] = string[idx]
            new_index -= 1

    return string

def urlify_2(string, length):

    # less verbose with split and not in place
    # runtime: O(n)
    new_str = string.split()
    return '%20'.join(new_str)    


class Test(unittest.TestCase):
    '''Test Cases'''
    # Using lists bc Python strings are immutable
    data = [
        (list('much ado about nothing      '), 22,
         list('much%20ado%20about%20nothing')),
        (list('Mr John Smith    '), 13, list('Mr%20John%20Smith'))]

    def test_urlify_1(self):
        for [test_string, length, expected] in self.data:
            actual = urlify_1(test_string, length)
            self.assertEqual(actual, expected)

class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        (('much ado about nothing      '), 22,
         ('much%20ado%20about%20nothing')),
        (('Mr John Smith    '), 13, ('Mr%20John%20Smith'))]

    def test_urlify_2(self):
        for [test_string, length, expected] in self.data:
            actual = urlify_2(test_string, length)
            self.assertEqual(actual, expected)            

if __name__ == "__main__":
    unittest.main()