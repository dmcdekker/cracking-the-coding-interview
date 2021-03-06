import unittest

def rotate_matrix(matrix):
    '''Rotate matrix left by 90 degrees'''
    outer = []
    inner = []
    # iterate through matrix to get first number of last inner array
    for idx in range(len(matrix)):
        # print idx
        for row in matrix[::-1]:
            print row[idx], '/'
            # append to inner arr
            inner.append(row[idx])
        # append content to outer array
        outer.extend([inner])    
        inner = []         
    return outer


class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ([
            [1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20],
            [21, 22, 23, 24, 25]
        ], [
            [21, 16, 11, 6, 1],
            [22, 17, 12, 7, 2],
            [23, 18, 13, 8, 3],
            [24, 19, 14, 9, 4],
            [25, 20, 15, 10, 5]
        ])
    ]

    def test_rotate_matrix(self):
        for [test_matrix, expected] in self.data:
            actual = rotate_matrix(test_matrix)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()