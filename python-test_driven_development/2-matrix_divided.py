#!/usr/bin/python3
"""function for matrix_divided method"""

def matrix_divided(matrix, div):
    """divdes all matrix elements by div"""
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) " +
                        "of integers/floats")
    
    """defining how the matrix will be on the row level"""
    for row in matrix:
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError("matrix must be a matrix (list of lists) " +
                            "of integers/floats")
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for x in row:
            if not isinstance(x, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) " +
                                "of integers/floats")
            
    """returns matrix-row with integers """
    return [[round(x / div, 2) for x in row] for row in matrix]

if __name__ == "__main__":
    """import doctest here becuase anywhere above will count as an import."""
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")