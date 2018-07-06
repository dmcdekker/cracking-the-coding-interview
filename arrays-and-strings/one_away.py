import unittest

def one_away(str1, str2):

    diff = len(str1) - len(str2)

    # difference greater than 1
    if abs(diff) > 1:
        return False

    # one str is longer than the other
    elif abs(diff) == 1:
        if diff == -1:
            for letter in str1:
                if letter not in str2:
                    return False
        else:
            for letter in str1:
                if letter not in str2:
                    return False

    # no difference in length
    else:
        count = 0
        for idx in range(len(str2)):
            if str1[idx] == str2[idx]:
                continue
            else:
                count += 1
                
        if count > 1:
            return False

    return True

class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ('pale', 'ple', True),
        ('pales', 'pale', True),
        ('pale', 'bale', True),
        ('paleabc', 'pleabc', True),
        ('pale', 'ble', False),
        ('a', 'b', True),
        ('', 'd', True),
        ('d', 'de', True),
        ('pale', 'pale', True),
        ('pale', 'ple', True),
        ('ple', 'pale', True),
        ('pale', 'bale', True),
        ('pale', 'bake', False),
        ('pale', 'pse', False),
        ('ples', 'pales', True),
        ('pale', 'pas', False),
        ('pas', 'pale', False),
        ('pale', 'pkle', True),
        ('pkle', 'pable', False),
        ('pal', 'palks', False),
        ('palks', 'pal', False)
    ]

    def test_one_away(self):
        for [test_s1, test_s2, expected] in self.data:
            actual = one_away(test_s1, test_s2)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()
