def in2cm(inches: float) -> float:
    ### BEGIN SOLUTION
    return inches * 2.54
    ### END SOLUTION

def cm2in(centimeters: float) -> float:
    ### BEGIN SOLUTION
    return centimeters / 2.54
    ### END SOLUTION

def ft2m(feet: float) -> float:
    ### BEGIN SOLUTION
    return feet * 0.3048
    ### END SOLUTION

def m2ft(meters: float) -> float:
    ### BEGIN SOLUTION
    return meters / 0.3048
    ### END SOLUTION

def yd2m(yards: float) -> float:
    ### BEGIN SOLUTION
    return yards * 0.9144
    ### END SOLUTION

def m2yd(meters: float) -> float:
    ### BEGIN SOLUTION
    return meters / 0.9144
    ### END SOLUTION

def mi2km(miles: float) -> float:
    ### BEGIN SOLUTION
    return miles * 1.609344
    ### END SOLUTION

def km2mi(kilometers: float) -> float:
    ### BEGIN SOLUTION
    return kilometers / 1.609344
    ### END SOLUTION



# l = range(-5,6)
# l1 = list(zip(l,map(ft2m, l)))
# l2 = list(zip(map(m2ft, l), l))

def test_feet():
    import math
    print('Testing feet............')
    tests = [(-5, -1.524),
             (-4, -1.2192),
             (-3, -0.9144000000000001),
             (-2, -0.6096),
             (-1, -0.3048),
             (0, 0.0),
             (1, 0.3048),
             (2, 0.6096),
             (3, 0.9144000000000001),
             (4, 1.2192),
             (5, 1.524),
             (-16.404199475065617, -5),
             (-13.123359580052492, -4),
             (-9.84251968503937, -3),
             (-6.561679790026246, -2),
             (-3.280839895013123, -1),
             (0.0, 0),
             (3.280839895013123, 1),
             (6.561679790026246, 2),
             (9.84251968503937, 3),
             (13.123359580052492, 4),
             (16.404199475065617, 5)]

    for feet, centimeters in tests:
        print(f'feet:{feet:+8.4f} meters:{centimeters: 8.4f}....', end='')
        meters = ft2m(feet)
        assert math.isclose(meters, centimeters), f'Error ft2m({feet})={meters}'
        feet_r = m2ft(centimeters)
        assert math.isclose(feet, feet_r), f'Error m2ft({centimeters})={feet_r}'
        print('OK')

#test_feet()

# l = range(-5,6)
# l1 = list(zip(l,map(yd2m, l)))
# l2 = list(zip(map(m2yd, l), l))

def test_yards():
    import math
    print('Testing yards............')
    tests = [(-5, -4.572),
             (-4, -3.6576),
             (-3, -2.7432),
             (-2, -1.8288),
             (-1, -0.9144),
             (0, 0.0),
             (1, 0.9144),
             (2, 1.8288),
             (3, 2.7432),
             (4, 3.6576),
             (5, 4.572),
             (-5.468066491688539, -5),
             (-4.374453193350831, -4),
             (-3.2808398950131235, -3),
             (-2.1872265966754156, -2),
             (-1.0936132983377078, -1),
             (0.0, 0),
             (1.0936132983377078, 1),
             (2.1872265966754156, 2),
             (3.2808398950131235, 3),
             (4.374453193350831, 4),
             (5.468066491688539, 5)]

    for yards, centimeters in tests:
        print(f'yards:{yards:+8.4f} meters:{centimeters: 8.4f}....', end='')
        meters = yd2m(yards)
        assert math.isclose(meters, centimeters), f'Error yd2m({yards})={meters}'
        yards_r = m2yd(centimeters)
        assert math.isclose(yards, yards_r), f'Error m2yd({centimeters})={yards_r}'
        print('OK')

#test_yards()

l = range(-5,6)
l1 = list(zip(l,map(mi2km, l)))
l2 = list(zip(map(km2mi, l), l))

def test_miles():
    import math
    print('Testing miles............')
    tests = [(-5, -8.04672),
             (-4, -6.437376),
             (-3, -4.828032),
             (-2, -3.218688),
             (-1, -1.609344),
             (0, 0.0),
             (1, 1.609344),
             (2, 3.218688),
             (3, 4.828032),
             (4, 6.437376),
             (5, 8.04672),
             (-3.1068559611866697, -5),
             (-2.485484768949336, -4),
             (-1.8641135767120018, -3),
             (-1.242742384474668, -2),
             (-0.621371192237334, -1),
             (0.0, 0),
             (0.621371192237334, 1),
             (1.242742384474668, 2),
             (1.8641135767120018, 3),
             (2.485484768949336, 4),
             (3.1068559611866697, 5)]

    for miles, kilometers in tests:
        print(f'miles:{miles:+8.4f} meters:{kilometers: 8.4f}....', end='')
        meters = mi2km(miles)
        assert math.isclose(meters, kilometers), f'Error mi2km({miles})={meters}'
        miles_r = km2mi(kilometers)
        assert math.isclose(miles, miles_r), f'Error km2yd({kilometers})={miles_r}'
        print('OK')

#test_miles()



def fhr2cel(fhr: float) -> float:
    ### BEGIN SOLUTION
    return ( fhr-32 )/1.8
    ### END SOLUTION

def cel2fhr(cel: float) -> float:
    ### BEGIN SOLUTION
    return 32 +  cel * 1.8
    ### END SOLUTION

def test_fhr():
    import math
    print('Testing fhr............')
    tests = [(-40, -40.0),
             (-30, -34.44444444444444),
             (-20, -28.88888888888889),
             (-10, -23.333333333333332),
             (0, -17.77777777777778),
             (10, -12.222222222222221),
             (20, -6.666666666666666),
             (30, -1.1111111111111112),
             (40, 4.444444444444445),
             (50, 10.0),
             (60, 15.555555555555555),
             (70, 21.11111111111111),
             (80, 26.666666666666664),
             (90, 32.22222222222222),
             (-40.0, -40),
             (-22.0, -30),
             (-4.0, -20),
             (14.0, -10),
             (32.0, 0),
             (50.0, 10),
             (68.0, 20),
             (86.0, 30),
             (104.0, 40),
             (122.0, 50),
             (140.0, 60),
             (158.0, 70),
             (176.0, 80),
             (194.0, 90)]

    for fhr, cel in tests:
        print(f'fhr:{fhr:+8.4f} cel:{cel: 8.4f}....', end='')
        cel = fhr2cel(fhr)
        assert math.isclose(cel, cel), f'Error mi2km({fhr})={cel}'
        fhr_r = cel2fhr(cel)
        assert math.isclose(fhr, fhr_r), f'Error km2yd({cel})={fhr_r}'
        print('OK')


import math

def circumference(radius: float) -> float:
    ### BEGIN SOLUTION
    return 2 * radius * math.pi
    ### END SOLUTION


def test_circumference():
    tests = [(0.0, 0.0),
            (0.5, 3.141592653589793),
            (1.0, 6.283185307179586),
            (1.5, 9.42477796076938),
            (2.0, 12.566370614359172),
            (2.5, 15.707963267948966),
            (3.0, 18.84955592153876),
            (3.5, 21.991148575128552),
            (4.0, 25.132741228718345),
            (4.5, 28.274333882308138),
            (5.0, 31.41592653589793)]
    for rad, length in tests:
        print(f'Testing {rad} {length}....', end='')
        res = circumference(rad)
        assert math.isclose(res, length), f'Error {rad} {length} {res}'
        print('OK')


def circle(radius: float) -> float:
    ### BEGIN SOLUTION
    return math.pi * radius**2
    ### END SOLUTION


def test_circle():
    tests = [(0.0, 0.0),
             (0.5, 0.7853981633974483),
             (1.0, 3.141592653589793),
             (1.5, 7.0685834705770345),
             (2.0, 12.566370614359172),
             (2.5, 19.634954084936208),
             (3.0, 28.274333882308138),
             (3.5, 38.48451000647496),
             (4.0, 50.26548245743669),
             (4.5, 63.61725123519331),
             (5.0, 78.53981633974483)]
    for rad, surface in tests:
        print(f'Testing {rad} {surface}....', end='')
        res = circle(rad)
        assert math.isclose(res, surface), f'Error {rad} {surface} {res}'
        print('OK')
