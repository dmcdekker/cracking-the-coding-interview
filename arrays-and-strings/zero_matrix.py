import unittest

def zero_matrix(matrix):
    '''Given an NxM matrix find the rows that contain a zero.'''
    zero_row = []
    zero_col = []
    for row_num, row in enumerate(matrix):
        for col_num, element in enumerate(row):
            if element == 0:
                zero_row.append(row_num)
                zero_col.append(col_num)


    #zero out rows
    for row in zero_row:
        for row_num in range(len(matrix[row])):
            matrix[row][row_num] = 0

    # zero out cols
    for col in zero_col:
        for col_num in range(len(matrix)):
            matrix[col_num][col] = 0

    return matrix  
    

    


class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ([
            [1, 2, 3, 4, 0],
            [6, 0, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 0, 18, 19, 20],
            [21, 22, 23, 24, 25]
        ], [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [11, 0, 13, 14, 0],
            [0, 0, 0, 0, 0],
            [21, 0, 23, 24, 0]
        ])
    ]

    def test_zero_matrix(self):
        for [test_matrix, expected] in self.data:
            actual = zero_matrix(test_matrix)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()