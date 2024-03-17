#!/usr/bin/python3
"""Function returns list of lists of integers
representing function for triangle n."""

def pascal_triangle(n):
    """This function is to represent Pascal's Triangle"""
    if n <= 0:
        return []
    
    triangles = [[1]]
    while len(triangles) != n:
        """Defining variables for the last integer of triangles and constant."""
        tri = triangles[-1]
        tmp = [1]
        for i in range(len(tri) - 1):
            """for loop starting from last triangle integer then appends other integers."""
            tmp.append(tri[i] + tri[i + 1])
        tmp.append(1)
        triangles.append(tmp)
    return triangles