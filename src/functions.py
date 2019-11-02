"""
This file contains two dicts of tuples,
with each tuple containing three lambdas.
For the first dict (mono, single rotations),
the rotation of the 6D cube is the key,
and the value tuple contains the functions
for module stages 1, 2, and 3 in that order.
The second dict (poly, multiple rotations)
has similar values, but the keys have to
be computed in solver.py based on which
axes the rotations involve (those rotations
are also passed as arguments for each of
the lambdas, as they utilize the lambdas
from the first dict to nest functions.
A helper method is used to put all of the
results between -364 and 364 inclusive.

:author: mythers45#1807 (Discord username)
"""

"""
MONO: Definitions of single (mono) rotation functions (5 args: x d n a b)
x is the number put into the function (a_n-1 for stage 1, b_n-1 for stage 2, c_n-1 for stage 3)
d is the constant sum of the base-36 digits in the serial number, notated in the manual as D
n is the position of this rotation in the sequence of rotations (from 1 to stage+2, a_4 = 0)
a is a_n-1, used in many functions for stages 2 and 3 (the same as x in stage 1)
b is b_n-1, used in many functions for stage 3 (the same as x in stage 2)
"""
mono = {"XY": ((lambda x, d, n, a, b: bound(x + d)),
               (lambda x, d, n, a, b: bound(x + a)),
               (lambda x, d, n, a, b: bound(x + b - a))),
        "XZ": ((lambda x, d, n, a, b: bound(2 * x - d)),
               (lambda x, d, n, a, b: bound(2 * x - a)),
               (lambda x, d, n, a, b: bound(2 * x - b - a))),
        "YZ": ((lambda x, d, n, a, b: bound(x + 2 * d)),
               (lambda x, d, n, a, b: bound(x + 2 * a)),
               (lambda x, d, n, a, b: bound(x + 2 * b - a))),
        "XW": ((lambda x, d, n, a, b: bound(2 * d - x)),
               (lambda x, d, n, a, b: bound(3 * d - x - a)),
               (lambda x, d, n, a, b: bound(4 * d - x - b - a))),
        "YW": ((lambda x, d, n, a, b: bound(2 * x + d - 35 * n)),
               (lambda x, d, n, a, b: bound(2 * x + abs(a) - 12 * n * n)),
               (lambda x, d, n, a, b: bound(2 * x + abs(b) + abs(a) - 5 * n * n * n))),
        "ZW": ((lambda x, d, n, a, b: bound(x + (x % 6) * (x % 6) * (x % 6))),
               (lambda x, d, n, a, b: bound(x + (a % 7) * (a % 7) * (a % 7))),
               (lambda x, d, n, a, b: bound(x + (b % 6) * (b % 6) * (b % 6) + (a % 6) * (a % 6) * (a % 6)))),
        "XV": ((lambda x, d, n, a, b: bound(2 * (d - x))),
               (lambda x, d, n, a, b: bound(2 * x - 3 * (d - a))),
               (lambda x, d, n, a, b: bound(2 * x - 4 * (d - b)))),
        "YV": ((lambda x, d, n, a, b: bound(x + (d % 6) * (d % 6) * (d % 6) - 35 * n)),
               (lambda x, d, n, a, b: bound(x + (a % 7) * (a % 7) * (a % 7) - 12 * n * n)),
               (lambda x, d, n, a, b: bound(x + (b % 8) * (b % 8) * (b % 8) - 5 * n * n * n))),
        "ZV": ((lambda x, d, n, a, b: bound((x - x % 2) / 2 + d)),
               (lambda x, d, n, a, b: bound(x + (x - x % 2) / 2 - a)),
               (lambda x, d, n, a, b: bound((x - x % n) / n + 2 * b))),
        "WV": ((lambda x, d, n, a, b: bound(5 * x - 3 * d)),
               (lambda x, d, n, a, b: bound(8 * x - 5 * d + 3 * a)),
               (lambda x, d, n, a, b: bound(13 * x - 8 * d + 5 * a - 3 * b))),
        "XU": ((lambda x, d, n, a, b: bound(x + 365 - d)),
               (lambda x, d, n, a, b: bound(x + 365 - abs(a))),
               (lambda x, d, n, a, b: bound(x + 365 - abs(a) - abs(b)))),
        "YU": ((lambda x, d, n, a, b: bound(2 * x - 365 + d)),
               (lambda x, d, n, a, b: bound(2 * x - 365 + abs(a))),
               (lambda x, d, n, a, b: bound(2 * x - 365 + abs(a) + abs(b)))),
        "ZU": ((lambda x, d, n, a, b: bound(x + 365 - 2 * d)),
               (lambda x, d, n, a, b: bound(x + 365 - 2 * abs(a))),
               (lambda x, d, n, a, b: bound(x + 365 - 2 * abs(a) - 2 * abs(b)))),
        "WU": ((lambda x, d, n, a, b: bound(365 - abs(x))),
               (lambda x, d, n, a, b: bound(365 - abs(x) - abs(a))),
               (lambda x, d, n, a, b: bound(365 - abs(x) - abs(a) - abs(b)))),
        "VU": ((lambda x, d, n, a, b: bound(n * x)),
               (lambda x, d, n, a, b: bound(n * (x - a))),
               (lambda x, d, n, a, b: bound(n * (x - a + b)))),
        "YX": ((lambda x, d, n, a, b: bound(x - d)),
               (lambda x, d, n, a, b: bound(x - a)),
               (lambda x, d, n, a, b: bound(x - b + a))),
        "ZX": ((lambda x, d, n, a, b: bound(2 * x + d)),
               (lambda x, d, n, a, b: bound(2 * x + a)),
               (lambda x, d, n, a, b: bound(b + a - 2 * x))),
        "ZY": ((lambda x, d, n, a, b: bound(x - 2 * d)),
               (lambda x, d, n, a, b: bound(x - 2 * a)),
               (lambda x, d, n, a, b: bound(x + 2 * a - b))),
        "WX": ((lambda x, d, n, a, b: bound(2 * d + x)),
               (lambda x, d, n, a, b: bound(3 * d + x - a)),
               (lambda x, d, n, a, b: bound(4 * d + x - b - a))),
        "WY": ((lambda x, d, n, a, b: bound(2 * x - d - 35 * n)),
               (lambda x, d, n, a, b: bound(2 * x - abs(a) - 12 * n * n)),
               (lambda x, d, n, a, b: bound(2 * x - abs(b) - abs(a) - 5 * n * n * n))),
        "WZ": ((lambda x, d, n, a, b: bound(x - (x % 7) * (x % 7) * (x % 7))),
               (lambda x, d, n, a, b: bound(x - (a % 6) * (a % 6) * (a % 6))),
               (lambda x, d, n, a, b: bound(x - (b % 7) * (b % 7) * (b % 7) - (a % 7) * (a % 7) * (a % 7)))),
        "VX": ((lambda x, d, n, a, b: bound(2 * (d + x))),
               (lambda x, d, n, a, b: bound(2 * x - 3 * (d + a))),
               (lambda x, d, n, a, b: bound(2 * x - 4 * (d + b)))),
        "VY": ((lambda x, d, n, a, b: bound(x - (d % 6) * (d % 6) * (d % 6) - 35 * n)),
               (lambda x, d, n, a, b: bound(x - (a % 7) * (a % 7) * (a % 7) - 12 * n * n)),
               (lambda x, d, n, a, b: bound(x - (b % 8) * (b % 8) * (b % 8) - 5 * n * n * n))),
        "VZ": ((lambda x, d, n, a, b: bound((x - x % 2) / 2 - d)),
               (lambda x, d, n, a, b: bound(x + (x - x % 2) / 2 + a)),
               (lambda x, d, n, a, b: bound((x - x % n) / n - 2 * b))),
        "VW": ((lambda x, d, n, a, b: bound(5 * x + 3 * d)),
               (lambda x, d, n, a, b: bound(8 * x + 5 * d - 3 * a)),
               (lambda x, d, n, a, b: bound(13 * x + 8 * d - 5 * a + 3 * b))),
        "UX": ((lambda x, d, n, a, b: bound(x - 365 - d)),
               (lambda x, d, n, a, b: bound(x - 365 - abs(a))),
               (lambda x, d, n, a, b: bound(x - 365 + abs(a) - abs(b)))),
        "UY": ((lambda x, d, n, a, b: bound(2 * x - 365 - d)),
               (lambda x, d, n, a, b: bound(2 * x - 365 - abs(a))),
               (lambda x, d, n, a, b: bound(2 * x - 365 + abs(a) - abs(b)))),
        "UZ": ((lambda x, d, n, a, b: bound(x + 365 + 2 * d)),
               (lambda x, d, n, a, b: bound(x + 365 + 2 * abs(a))),
               (lambda x, d, n, a, b: bound(x + 365 + 2 * abs(a) - 2 * abs(b)))),
        "UW": ((lambda x, d, n, a, b: bound(365 - 2 * abs(x))),
               (lambda x, d, n, a, b: bound(365 - 2 * abs(x) - abs(a))),
               (lambda x, d, n, a, b: bound(365 - 2 * abs(x) - abs(a) - abs(b)))),
        "UV": ((lambda x, d, n, a, b: bound(n * x - d)),
               (lambda x, d, n, a, b: bound(n * (x - a - d))),
               (lambda x, d, n, a, b: bound(n * (x - a - b))))}

"""
POLY: Definitions of multiple (poly) rotation functions (8 args: x d n a b r s t)
x, d, n, a, and b share the same meanings from the mono dictionary (above)
r is one of the two or three rotations in the multiple rotation
s is another of the two or three rotations, like r (order doesn't matter!)
t is only used if there are three rotations, where it's the third one of the trio
"""
poly = {"X":  ((lambda x, d, n, a, b, r, s, t: bound(2*d-abs(mono[r][0](x, d, n, a, b)
                                                             - mono[s][0](x, d, n, a, b)))),
               (lambda x, d, n, a, b, r, s, t: bound(3*d-abs(mono[r][1](x, d, n, a, b)
                                                             + mono[s][1](x, d, n, a, b)))),
               (lambda x, d, n, a, b, r, s, t: bound(4*d-abs(mono[r][2](x, d, n, a, b))
                                                     - abs(mono[s][2](x, d, n, a, b))))),
        "Y":  ((lambda x, d, n, a, b, r, s, t: bound(2*d-mono[r][0](x, d, n, a, b)
                                                     - mono[s][0](x, d, n, a, b))),
               (lambda x, d, n, a, b, r, s, t: bound(2*a-mono[r][1](x, d, n, a, b)
                                                     - mono[s][1](x, d, n, a, b))),
               (lambda x, d, n, a, b, r, s, t: bound(2*b-mono[r][2](x, d, n, a, b)
                                                     - mono[s][2](x, d, n, a, b)))),
        "Z":  ((lambda x, d, n, a, b, r, s, t: bound(mono[r][0](x, d, n, a, b)
                                                     + mono[s][0](x, d, n, a, b)-x)),
               (lambda x, d, n, a, b, r, s, t: bound(mono[r][1](x, d, n, a, b)
                                                     + mono[s][1](x, d, n, a, b)-x-a)),
               (lambda x, d, n, a, b, r, s, t: bound(mono[r][2](x, d, n, a, b)
                                                     + mono[s][2](x, d, n, a, b)-x-b-a))),
        "W":  ((lambda x, d, n, a, b, r, s, t: bound(max(mono[r][0](x, d, n, a, b),
                                                         mono[s][0](x, d, n, a, b),
                                                         mono[t][0](x, d, n, a, b))-2*d)),
               (lambda x, d, n, a, b, r, s, t: bound(mono[r][1](x, d, n, a, b)
                                                     + mono[s][1](x, d, n, a, b)
                                                     + mono[t][1](x, d, n, a, b)-2*x)),
               (lambda x, d, n, a, b, r, s, t: bound(mono[r][2](x, d, n, a, b)
                                                     + mono[s][2](x, d, n, a, b)
                                                     + mono[t][2](x, d, n, a, b)-a-b-x))),
        "V":  ((lambda x, d, n, a, b, r, s, t: bound(min(mono[r][0](x, d, n, a, b),
                                                         mono[s][0](x, d, n, a, b),
                                                         mono[t][0](x, d, n, a, b))+2*d)),
               (lambda x, d, n, a, b, r, s, t: bound(2*x-mono[r][1](x, d, n, a, b)
                                                     - mono[s][1](x, d, n, a, b)
                                                     - mono[t][1](x, d, n, a, b))),
               (lambda x, d, n, a, b, r, s, t: bound(a+b+x-mono[r][2](x, d, n, a, b)
                                                     - mono[s][2](x, d, n, a, b)
                                                     - mono[t][2](x, d, n, a, b))))}


def bound(x: int) -> int:
    """
    Takes the result of a function and takes it modulo 365,
    but if the original number was negative and the result
    of the modulo wasn't zero, subtracts 365 from the result.
    This puts the number between -364 and 364 inclusive.
    :param x: The number to bound
    :return: The bounded number
    """
    y = x % 365  # Begin by taking x modulo 365 where the result is positive.
    if x < 0 < y:  # If x was negative, and y was not 0 (y can't be negative)...
        return y - 365  # Subtract 365 from y, putting it to -364 at the lowest.
    return y  # Otherwise, just return y (if y was 0, this line executes).