def runtests(tests, fun):
    for test, ex_res in tests:
        print(f'"{test}", "{ex_res}"....', end='')
        res = fun(*test)
        assert res == ex_res, f'Error, the result is "{res}"'
        print('OK.')
