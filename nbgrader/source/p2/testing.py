from functools import total_ordering

@total_ordering
class WrapperStr(str):
    def __init__(self, s: str):
        self.str = s
    def __eq__(self, other):
            if len(self.str)!=1 or len(other)!=1:
                raise Exception(f'It is illegal to compare strings of lengh greater than 1: "{self.str}", "{other.str}"')
            return self.str==other
    def __le__(self, other):
            if len(self.str)!=1 or len(other)!=1:
                raise Exception(f'It is illegal to compare strings of lengh greater than 1: "{self.str}", "{other.str}"')
            return self.str<other

    def __contains__(self, item):
            raise Exception(f'Illegal call to "in"')
    def __getitem__(self, key):
        if not isinstance(key, int):
            raise Exception(f'Illegal call [{key}]')
        return self.str[key]

    def lower(self):
        raise Exception('Illegal call')

@total_ordering
class WrapperLst(list):
    def __init__(self, l: list):
        self.list = l

    def __eq__(self, other):
        raise Exception('It is illegal to compare lists')

    def __le__(self, other):
        raise Exception('It is illegal to compare lists')

    def __contains__(self, item):
            raise Exception(f'Illegal call to "in"')

    def __getitem__(self, key):
        if not isinstance(key, int):
            raise Exception(f'Illegal call [{key}]')
        return self.list[key]


def runtests(tests, fun):
    for test, ex_res in tests:
        print(f'"{test}", "{ex_res}"....', end='')
        res = fun(*test)
        assert res == ex_res, f'Error, the result is "{res}"'
        print('OK.')
