#!/usr/bin/python3
'''pascal triangle'''


def factorial(n):
    '''computes factorial of n'''
    if n == 0:
        return 1
    num = 1
    for i in range(1, n + 1):
        num *= i
    return num


def combination(n, r):
    '''finds combination of (n, r)'''
    return (factorial(n) // (factorial(r) * factorial(n - r)))


def pascal_tringle(n):
    '''the pascal tringle of given n'''
    triangle = []
    for i in range(n + 1):
        temp = []
        for j in range(0, i + 1):
            temp.append(combination(i, j))
        triangle.append(temp)
    return triangle
