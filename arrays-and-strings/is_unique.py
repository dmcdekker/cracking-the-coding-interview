import unittest

# Implement algorithm to determine if string has all unique chars
# What if you cannot use additional data structures?

def is_unique(string):
    '''Check if string contains unique characters'''
    
    # for ASCII char set
    if len(string) > 128:
        return False

    # use set
    # runtime: O(n)
    
    if len(string) > len(set(string)):
        return False
    return True

    # using while loop
    # runtime: O(n)
    # idx1 = 0
    # while idx1 < len(string):
    #     idx2 = 0
    #     if idx1 != idx2 and string[idx1] == string[idx2]:
    #         return False
    #     else:
    #         idx2 +=1
    #     idx1 += 1
    # return True            


    # using for loop 
    # runtime: O(n^2)
    # for idx1, item in enumerate(string):
    #     for idx2, item in enumerate(string):
    #         if idx1 != idx2 and string[idx1] == string[idx2]:
    #             return False
    # return True 
     

class Test(unittest.TestCase):
    test1= [('abcd'), ('s4fad'), ('')]
    test2 = [('23ds2'), ('hb 627jh=j ()')]

    def test_unique(self):
        # true check
        for test_string in self.test1:
            actual = is_unique(test_string)
            self.assertTrue(actual)
        # false check
        for test_string in self.test2:
            actual = is_unique(test_string)
            self.assertFalse(actual)

if __name__ == "__main__":
    unittest.main()




