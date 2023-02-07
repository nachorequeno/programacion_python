import math
import inspect
from copy import deepcopy as copy
import matrices

def runtests(tests, fun, equals=lambda x,y: x==y, keep_originals=False):
    for test, ex_res in tests:
        print(f'"{test}", "{ex_res}"....', end='')
        if inspect.isclass(ex_res) and issubclass(ex_res, Exception):
            error_type = type(ex_res)
            try:
                res = fun(*test)
            except ex_res:
                print('OK')
            else:
                 assert False, 'The arguments are illegal and not detected'
        else:
            if keep_originals:
                test_ori = copy(test)
            res = fun(*test)
            assert equals(res, ex_res), f'Error, the result is "{res}"'
            if keep_originals:
                assert test==test_ori, f'The originals values has been modified: {test} {test_ori}'
            print('OK.')

def test_equal_matrix(mat1: list[list[float]], mat2: list[list[float]]) -> bool:

    nrows = len(mat1)
    ncols = len(mat1[0])
    eq = True
    i = 0
    while eq and i < len(mat1):
        j =0
        while eq and j < len(mat1[0]):
            assert math.isclose(mat1[i][j], mat2[i][j]), f'positions ({i}, {j}) differs, {mat1[i][j]}, {mat2[i][j]}'
            j += 1
        i += 1
    return eq


def test_is_correct_matrix():
    tests = [
        ( ([],), False),
        ( ([[]],), False),
        ( ([[1]],), True),
        ( ([[1,2]],), True),
        ( ([[1,2],[2,3]],), True),
        ( ([[1,2],[2,3],[3,4]],), True),
        ( ([[1,2],[2]],), False),
        ( ([[1],[2,3]],), False),
        ( ([[1],[2,3],[3,4]],), False),
        ( ([[1,2],[2],[3,4]],), False),
        ( ([[1,2],[2,3],[3]],), False),
        ( ([[1,2],[],[3,4]],), False),
        ( ([[1,2],[2,3],[]],), False),
    ]
    runtests(tests, matrices.is_correct_matrix, keep_originals=True)

# def test_create_matrix():
#     def auxtest_matrix(m, nrows, ncols):
#         assert len(m) == nrows, \
#             f'incorrect number of rows: {len(m)}, {nrows}'
#         for i in range(len(m)):
#             assert len(m[i]) == ncols, \
#                 f'incorrect number of rows: {len(m[i])}, {ncols}'
#             for j in range(len(m[i])):
#                 assert type(m[i][j]) == float, \
#                     'The elements must be float'
#                 assert math.isclose(m[i][j], 0), \
#                     f'Incorrect element {m[i][j]}'
#         fill_matrix(m)
#         elem = 0
#         for i in range(len(m)):
#             for j in range(len(m[i])):
#                 assert math.isclose(m[i][j], elem), \
#                     f'Incorrect element {m[i][j]} {elem}'
#                 elem += 1
#     sizes = [(2, 3), (3, 2), (5, 3), (3, 5), (5, 5)]
#     for nrows, ncols in sizes:
#         m = create_matrix(nrows, ncols)
#         auxtest_matrix(m, nrows, ncols)
#     print('OK')

def test_create_matrix():
    tests = [
        ((0, 1), AssertionError),
        ((1, 0), AssertionError),
        ((2, 3), [[0]*3, [0]*3]),
        ((3, 2), [[0]*2, [0]*2, [0]*2]),
        ((5, 3), [[0]*3, [0]*3, [0]*3, [0]*3, [0]*3]),
        ((3, 5), [[0]*5, [0]*5, [0]*5]),
        ((5, 5), [[0]*5, [0]*5, [0]*5, [0]*5, [0]*5]),
    ]
    runtests(tests, matrices.create_matrix, equals=test_equal_matrix)


def test_copy_matrix():
    tests = [
        (([], ), AssertionError),
        (([[]], ), AssertionError),
        (([ [1, 2], [3, 2] ],), [ [1, 2], [3, 2] ]),
        (([ [1, 2, 4], [3, 2, 5] ],), [ [1, 2, 4], [3, 2, 5] ]),
        (([ [1, 2], [4, 5], [3, 2] ],), [ [1, 2],[4, 5], [3, 2] ])
    ]
    runtests(tests, copy_matrix, equals=test_equal_matrix, keep_originals=True)

# def test_copy_matrix():
#     def auxtext_cpm(mat):
#         m1 = copy_matrix(mat)
#         for i in range(len(mat)):
#             for j in range(len(mat[0])):
#                 assert math.isclose(mat[i][j], m1[i][j]), \
#                     f'error {i}, {j}, {mat[i][j]}, m1[i][j]'
#                 m1[i][j] += 1
#                 assert not math.isclose(mat[i][j], m1[i][j]), \
#                     f'error {i}, {j}, {mat[i][j]}, m1[i][j]'
#     mats = [
#         [
#             [1, 2],
#             [3, 2]
#         ],
#         [
#             [1, 2, 4],
#             [3, 2, 5]
#         ],
#         [
#             [1, 2],
#             [4, 5],
#             [3, 2]
#         ]
#     ]

#     for mat in mats:
#         auxtext_cpm(mat)
#     print('OK.')

def test_are_equal():
    tests = [
        (([], [[1]]), AssertionError),
        (([[1]], []), AssertionError),
        (([[1]], [[1,2]]), AssertionError),
        (([[1,2]], [[1]]), AssertionError),
        (([[1,2],[2]], [[1,2],[2,3]]), AssertionError),
        (([[1,2],[2,3]], [[1,2],[2]]), AssertionError),
        (([[1,2],[2,3]], [[1,2,4],[2,3,4]]), AssertionError),
        (([[1,2],[2,3],[4,5]], [[1,2],[2,3,4]]), AssertionError),
        (([[2]], [[math.sqrt(2)**2]]), True),
        (([[1,2],[2,3],[4,5]], [[1,2],[2,3],[4,5]]), True),
        (([[1,2],[1,3],[4,5]], [[1,2],[2,3],[4,5]]), False),
        (([[1,2],[2,3],[1,5]], [[1,2],[2,3],[4,5]]), False),
        (([[1,2],[2,3],[4,1]], [[1,2],[2,3],[4,5]]), False),
        (([[1,1],[2,3],[4,5]], [[1,2],[2,3],[4,5]]), False),
    ]
    runtests(tests, matrices.are_equal_matrix, keep_originals=True)


def test_transpose():
    def auxtext_trps(mat):
        m1 = matrices.transpose(mat)
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                assert math.isclose(mat[i][j], m1[j][i]), \
                    f'error {i}, {j}, {mat[i][j]}, m1[j][i]'
                m1[j][i] += 1
                assert not math.isclose(mat[i][j], m1[j][i]), \
                    f'error {i}, {j}, {mat[i][j]}, m1[j][i]'
    mats = [
        [
            [1, 2],
            [3, 2]
        ],
        [
            [1, 2, 4],
            [3, 2, 5]
        ],
        [
            [1, 2],
            [4, 5],
            [3, 2]
        ]
    ]

    for mat in mats:
        auxtext_trps(mat)
    print('OK.')




def test_add():
    tests = [
        (([], [[1]]), AssertionError),
        (([[1]], []), AssertionError),
        (([[1]], [[1,2]]), AssertionError),
        (([[1,2]], [[1]]), AssertionError),
        (([[1,2],[2]], [[1,2],[2,3]]), AssertionError),
        (([[1,2],[2,3]], [[1,2],[2]]), AssertionError),
        (([[1,2],[2,3]], [[1,2,4],[2,3,4]]), AssertionError),
        (([[1,2],[2,3],[4,5]], [[1,2],[2,3,4]]), AssertionError),
        (([[1,2],[3,4]], [[4,3],[2,1]]), [[5,5],[5,5]])
    ]


    runtests(tests, matrices.add, test_equal_matrix, keep_originals=True)


def test_is_symmetric():
    tests = [
        (([], ), AssertionError),
        (([[1]], ), True),
        (([[1, 2], [2]], ), AssertionError),
        (([[1, 2], [2, 3]], ), True),
        (([[1, 1], [2, 3]], ), False),
        (([[1, 2, 4], [2, 3, 4]], ), False),
        (([[1, 2], [2, 3], [4, 5]], ), False),
        (([[1, 2], [math.sqrt(2)**2, 1]], ), True)
    ]
    runtests(tests, matrices.is_symmetric, keep_originals=True)



def test_mult():
    tests = [
        (([], [[1]]), AssertionError),
        (([[1]], []), AssertionError),
        (([[1]], [[1,2]]), [[1,2]]),
        (([[1,2]], [[1]]), AssertionError),
        (([[1,2],[2]], [[1,2],[2,3]]), AssertionError),
        (([[1,2],[2,3]], [[1,2],[2]]), AssertionError),
        (([[1,2],[2,3]], [[1,2,4],[2,3,4]]), [[5,8,12], [8, 13, 20]]),
        (([[1,2,4],[2,3,4]], [[1,2],[2,3]]), AssertionError),
        (([[1,2],[2,3],[4,5]], [[1,2],[2,3,4]]), AssertionError),
        (([[1,2],[3,4]], [[4,3],[2,1]]), [[8,5], [20, 13]])
    ]


    runtests(tests, matrices.mult, test_equal_matrix, keep_originals=True)




def test_determinant():
    tests = [
        (([], ), AssertionError),
        (([[1]], ), 1),
        (([[1, 2], [2]], ), AssertionError),
        (([[1, 2], [2, 3]], ), -1),
        (([[1, 1], [2, 3]], ), 1),
        (([[1, 2, 4], [2, 3, 4]], ), AssertionError),
        (([[1, 2], [2, 3], [4, 5]], ), AssertionError),
        (([[1, 2], [math.sqrt(2)**2, 1]], ), -3),
        (([[0,0],[0,0]], ), 0),
        (([[1,1,1],[1,1,1],[1,1,1]], ), 0),
        (([[-2, -1, 2], [2,1,4], [-3,3,-1]],), 54)
    ]
    runtests(tests, matrices.determinant, equals=math.isclose, keep_originals=True)
