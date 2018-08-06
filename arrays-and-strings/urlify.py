import unittest

def urlify_1(string, length):
    '''Replace all spaces in a string with %20''' 
    # turn string into list 
    str_as_list = list(string)
    # get length of str
    lst_len = len(str_as_list) -1
    # start iterating at end of list (common practice)
    for idx in range(length - 1, -1, -1):
        # if char isn't single space: eliminate all extra space
        if(str_as_list[idx] != ' '):
            # make char last space in list
            str_as_list[lst_len] = str_as_list[idx]
            # end of list is minus 1 char
            lst_len -= 1
        else:
            # if empty space: add chars 
            str_as_list[lst_len] = '0'
            str_as_list[lst_len-1] = '2'
            str_as_list[lst_len-2] = '%'
            # end of list is minus 3 chars
            lst_len -= 3

    return ''.join(str_as_list)

    # Runtime = O(n)

# def urlify_2(string, length):

#     # less verbose with split and not in place
#     # runtime: O(n)
#     new_str = string.split()
#     return '%20'.join(new_str)    

class Test(unittest.TestCase):
    '''Test Cases'''
    # Using lists because Python strings are immutable
    data = [
        (('much ado about nothing      '), 22,
         ('much%20ado%20about%20nothing')),
        (('Mr John Smith    '), 13, ('Mr%20John%20Smith'))]

    def test_urlify(self):
        for [test_string, length, expected] in self.data:
            actual = urlify_1(test_string, length)
            self.assertEqual(actual, expected)


# class Test(unittest.TestCase):
#     '''Test Cases'''
#     data = [
#         (('much ado about nothing      '), 22,
#          ('much%20ado%20about%20nothing')),
#         (('Mr John Smith    '), 13, ('Mr%20John%20Smith'))]

#     def test_urlify_2(self):
#         for [test_string, length, expected] in self.data:
#             actual = urlify_2(test_string, length)
#             self.assertEqual(actual, expected)            

if __name__ == "__main__":
    unittest.main()