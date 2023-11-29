#!/usr/bin/python3
''' matrix implementation'''


def matrix_mul(m_a, m_b):
    '''matrix to  matrix multiplication'''

    if type(m_a) is list:
        if len(m_a) == 0:
            raise ValueError("m_a can't be empty")
        if type(m_a[0]) is not list:
            raise TypeError("m_a must be a list of lists")
        size = len(m_a[0])
        for inner in m_a:
            if type(inner) is not list:
                raise TypeError("m_a must be a list of lists")
            if len(inner) != size:
                raise TypeError("each row of m_a must be of the same size")
            if len(inner) == 0:
                raise ValueError("m_a can't be empty")
            for i in inner:
                if type(i) is not int or type(i) is not int:
                    raise TypeError("m_a should contain\
 only integers or floats")
    else:
        raise TypeError("m_a must be a list")

    if type(m_b) is list:
        if len(m_b) == 0:
            raise ValueError("m_b can't be empty")
        if type(m_b[0]) is not list:
            raise TypeError("m_b must be a list of lists")
        size = len(m_b[0])
        for inner in m_b:
            if type(inner) is not list:
                raise TypeError("m_b must be a list of lists")
            if len(inner) != size:
                raise TypeError("each row of m_b must be of the same size")
            if len(inner) == 0:
                raise ValueError("m_b can't be empty")
            for i in inner:
                if type(i) is not int or type(i) is not int:
                    raise TypeError("m_b should contain\
 only integers or floats")
    else:
        raise TypeError("m_b must be a list")

    rowA, colA = len(m_a), len(m_a[0])
    rowB, colB = len(m_b), len(m_b[0])
    if colA != rowB:
        raise ValueError("m_a and m_b can't be multiplied")

    result = []
    for i in range(rowA):
        temp = []
        for j in range(colB):

            num = 0
            for k in range(colA):
                num += (m_a[i][k] * m_b[k][j])
            temp.append(num)
        result.append(temp)

    return result
