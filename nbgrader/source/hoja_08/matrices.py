"""
Module with functions for matrices

@author: Luis Llana
@year: 2023
"""

import math


def create_matrix(nrows: int, ncols: int) -> list[list[float]]:
    """
    This function creates a nrows x ncols matrix of zeroes
    """

    assert nrows > 0 and ncols > 0, \
        f'The number of rows and cols must be positive {nrows} {ncols}'
    mat = []
    for _ in range(nrows):
        mat.append([0.0] * ncols)
    return mat


def fill_matrix(m: list[list[float]]):
    elem = 0.0
    for i in range(len(m)):
        for j in range(len(m[i])):
            m[i][j] = elem
            elem += 1

def repr_matrix(matrix: list[list[float]]) -> str:
    """
    Procedure to transform a real number matrix into a str.
    We do not requiere that is a well form matrix.
    """
    if len(matrix) == 0 or len(matrix[0]) == 0:
        s = f'Incorrect list: {matrix}'
    else:
        s = f'matrix {len(matrix)}x{len(matrix[0])}\n'
        for row in matrix:
            s += '|'
            for cell in row:
                s += "{0:.2f}  ".format(cell)
            s += '|\n'
    return s


def is_correct_matrix(mat: list[list[float]]) -> bool:
    res = len(mat)>0 and len(mat[0])>0
    i = 1
    while res and i<len(mat):
        res = len(mat[0]) == len(mat[i])
        i += 1
    return res


def are_equal_matrix(mat1: list[list[float]], mat2: list[list[float]]) -> bool:
    '''
    Compares to matrixes of the same size. Sin the elements are float, the functione uses
    math.isclose to compare the elements
    '''
    assert is_correct_matrix(mat1) and is_correct_matrix(mat2) and \
        len(mat1)==len(mat2) and \
        len(mat1[0])==len(mat2[0]), \
        f'incorrect arguments:\n {repr_matrix(mat1)}\n--------\n{repr_matrix(mat2)} '

    nrows = len(mat1)
    ncols = len(mat1[0])
    eq = True
    i = 0
    while eq and i < len(mat1):
        j =0
        while eq and j < len(mat1[0]):
            eq = math.isclose(mat1[i][j], mat2[i][j])
            j += 1
        i += 1
    return eq


def is_square(mat: list[list[float]]) -> bool:
    '''
    Checks if the matrix is square
    '''
    assert is_correct_matrix(mat), \
        f'incorrect arguments:\n {repr_matrix(mat)}'
    nrows = len(mat)
    ncols = len(mat[0])
    return ncols == nrows

def is_symmetric(mat: list[list[float]]) -> bool:
    '''
    Checks if mat is simmetric. If mat is not a square matrix, returns False
    '''
    assert is_correct_matrix(mat), \
        f'incorrect arguments:\n {repr_matrix(mat)}'
    nrows = len(mat)
    if is_square(mat):
        i = 0
        res = True
        while i < nrows and res:
            j = i+1
            while res and j < nrows:
                res = math.isclose(mat[i][j], mat[j][i])
                #print(f'c1, {i} {j} {mat[i][j]} {mat[i][j]}, {res}')
                j = j+1
            i = i+1
    else:
        res = False
    return res


def copy_matrix(mat: list[list[float]]) -> list[list[float]]:
    """
    Makes a copy of mat.

    Precondition:
    =============
    mat is a matrix: a list whose elements are list of the same lenght
    """

    assert is_correct_matrix(mat), f'Cannot copy an incorrect matrix'
    new_mat = create_matrix(len(mat), len(mat[0]))
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            new_mat[i][j] = mat[i][j]
    return new_mat


def transpose(matrix: list[list[float]]) -> list[list[float]]:
    """Function that transpose a matrix. This function
    returns a new matrix. It does not modify the original one
    """
    assert is_correct_matrix(matrix), f'inctorrect matrix {repr_matrix(matrix)}'
    rows = len(matrix)
    cols = len(matrix[0])
    new = create_matrix(cols, rows)
    i = 0
    while i<rows:
        j = 0
        while j<cols:
            new[j][i] = matrix[i][j]
            j += 1
        i += 1
    return new


def add(mat1: list[list[float]], mat2: list[list[float]]) -> list[list[float]]:
    """Function that computes the sum of matrices mat1 and mat2

    mat1: non empty matrix of numbers of size n x m
    mat2: non empty matrix of numbers of size n x m
    result a matrix of size n x m
    """
    assert is_correct_matrix(mat2), f'inctorrect matrix {repr_matrix(mat1)}'
    assert is_correct_matrix(mat1), f'inctorrect matrix {repr_matrix(mat2)}'
    assert len(mat1)==len(mat2) and len(mat1[0])==len(mat2[0]), \
        'The sizes of the matrixes does not match {len(mat1)}x{len(mat1[0])} and {len(mat1)}x{len(mat1[0])} '
    nrows = len(mat1)
    ncols = len(mat1[0])
    new = create_matrix(nrows, ncols)
    for i in range(nrows):
        for j in range(ncols):
            new[i][j] = mat1[i][j] + mat2[i][j]
    return new


def mult(mat1: list[list[float]], mat2: list[list[float]]) -> list[list[float]]:
    """Function that computes the multiplication of matrices mat1 and mat2

    mat1: non empty matrix of numbers of size n x k
    mat2: non empty matrix of numbers of size k x m
    result: a matrix of size n x m
    """
    assert is_correct_matrix(mat2), f'inctorrect matrix {repr_matrix(mat1)}'
    assert is_correct_matrix(mat1), f'inctorrect matrix {repr_matrix(mat2)}'
    assert len(mat1[0])==len(mat2), \
        'The sizes of the matrixes does not match {len(mat1)}x{len(mat1[0])} and {len(mat1)}x{len(mat1[0])} '

    rows = len(mat1)
    cols = len(mat2[0])
    common = len(mat2)
    new = create_matrix(rows, cols)
    i = 0
    while i < rows:
        j = 0
        while j < cols:
            k = 0
            elem = 0.0
            while k < common:
                elem += mat1[i][k]*mat2[k][j]
                k = k+1
            new[i][j] = elem
            j = j+1
        i = i+1
    return new




def find_non_null(matrix, col):
    """
    This function returns the row of the first non-null
    element of the column col in the matrix starting from row=col.
    If that element
    does not exist, the function returns len(marix)

    Parameters
    ----------
    matrix: list of list of numbers
    col: int

    Precondition
    ------------
    matrix: non empty matrix of size n x n (square matrix)
    col: 0<=col<len(matrix)
    """

    i = col
    while i < len(matrix) and  math.isclose(matrix[i][col], 0.0):
        i += 1
    return i


def change_row(matrix, row1, row2):
    """
    Parameters
    ----------
    matrix: list of list of numbers
    col: int

    Precondition
    ------------
    matrix: non empty matrix of size n x n (square matrix)
    0<=row1, row2<len(matrix)
    """
    len_row = len(matrix)
    for i in range(len_row):
        aux = matrix[row1][i]
        matrix[row1][i] = matrix[row2][i]
        matrix[row2][i] = aux

def divive_row(matrix, row, value):
    """
    value!=0
    """
    for i in range(len(matrix)):
          matrix[row][i] = matrix[row][i] / value

def combine_rows(matrix, row, col, val):
    """

    Parameters
    ----------
    matrix: list of list of numbers
    col: int

    Precondition
    ------------
    matrix: non empty matrix of size n x n (square matrix)
    col: 0<=col<len(matrix)
    matrix[col][col]=1
    """
    i = 0
    while i<len(matrix):
        matrix[row][i] -= val * matrix[col][i]
        i += 1

def pivot(matrix, col):
    """

    Parameters
    ----------
    matrix: list of list of numbers
    col: int

    Precondition
    ------------
    matrix: non empty matrix of size n x n (square matrix)
    col: 0<=col<len(matrix)

    Returns
    float: the element in the diagonal
    """
    row = find_non_null(matrix, col)
    if row==len(matrix):
        val = 0
    else:
        if (row + col) % 2 == 0:
            sg = 1
        else:
            sg =-1
        change_row(matrix, row, col)
        val = sg * matrix[col][col]
        divive_row(matrix, col, matrix[col][col])
        i = 0
        while i<len(matrix):
            if i!=col:
                factor = matrix[i][col]
                combine_rows(matrix, i, col, factor)
            i += 1
    return val

def determinant(matrix):
    """
    computes the determinat of a square matrix matrix:
    """
    assert is_correct_matrix(matrix) and is_square(matrix), \
        f'the determinant can only be computed on a square matrix'

    # with this procedure the matrix will change.
    # since we do not want to change the original matrix
    # we need to operate over a copy.
    aux = copy_matrix(matrix)
    size = len(matrix)
    det = 1
    i = 0
    while i<size:
        val = pivot(aux, i)
        det = det * val
        i += 1
    return det
