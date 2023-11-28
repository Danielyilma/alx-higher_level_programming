#!/usr/bin/python3


'''
implementing division of matrix by integer
the matrix has a list of integers in form of lists
'''
def matrix_divided(matrix, div):
    '''
    matrix division returns matrix of the division in their repective position
    '''
    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    else:
        size = len(matrix[0])
        for i in matrix:
            if type(i) is list:
                if size != len(i):
                    raise TypeError("Each row of the matrix must have the same size")
                for j in i:
                    if type(j) is not int and type(j) is not float:
                        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            else:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    
    result = []
    temp = []

    for item in matrix:
        for i in item:
            temp.append(round(i/div, 2))
        result.append(temp)
        temp = []

    return result

