import numpy as np

pathin, pathpol, pathout = "input.txt", "polynom.txt", "output.txt"


def Addition(sl, sr):
    lhs = [int(item) for item in sl]
    rhs = [int(item) for item in sr]
    with open(pathout, "w") as f:
        if len(lhs) > len(rhs):
            for i in range(len(rhs)):
                lhs[i] = (lhs[i] + rhs[i]) % 2
            f.write("".join(str(x) for x in lhs))
        else:
            for i in range(len(lhs)):
                rhs[i] = (lhs[i] + rhs[i]) % 2
            f.write("".join(str(x) for x in rhs))


def Multiplication(sl, sr, pol):
    pol = [int(item) for item in pol]
    lhs = [int(item) for item in sl]
    rhs = [int(item) for item in sr]
    result = [0] * (len(lhs) + len(rhs))
    for i, item1 in enumerate(lhs):
        for j, item2 in enumerate(rhs):
            result[i + j] = (result[i + j] + item1 * item2) % 2
    result.reverse()
    pol.reverse()
    _, r = np.polydiv(result, pol)
    r = r.tolist()
    r.reverse()
    r = [(int(item) % 2) for item in r]
    with open(pathout, 'w') as f:
        f.write("".join(str(x) for x in r))
        return "".join(str(x) for x in r)


def Division(sl, sr, pol):
    rhs = Reverse(sr, pol)
    Multiplication(sl, "".join(str(x) for x in rhs), pol)


def Reverse(sl, sr):
    if len(sl) < len(sr):
        lhs = [int(item) for item in sl]
        rhs = [int(item) for item in sr]
    else:
        rhs = [int(item) for item in sl]
        lhs = [int(item) for item in sr]
    rhs.reverse()
    lhs.reverse()
    x, y = [0], 0
    l = list()
    while True:
        q, r = np.polydiv(rhs, lhs)
        q = q.tolist()
        l.append([int(item) for item in q])
        rhs = lhs
        lhs = r
        if len(r) == 1:
            y = pow(int(r.tolist()[0]), -1, 2)
            break
    y = [y]
    for i in range(len(l)):
        new_y = np.polysub(x, np.polymul(y, l[len(l) - i - 1]))
        x = y
        y = new_y
    y = y.tolist()
    y.reverse()
    y = [(int(item) % 2) for item in y]
    with open(pathout, 'w') as f:
        f.write("".join(str(x) for x in y))
        return y


def Exponentiation(sl, sr, pol):
    l = sl
    for _ in range(int(sr) - 1):
        l = Multiplication(l, sl, pol)
    with open(pathout, 'w') as f:
        f.write(l)


def Calculate(s):
    items = s.split()
    if items[1] == "+":
        Addition(items[0], items[2])
    elif items[1] == "*":
        with open(pathpol, "r") as f:
            Multiplication(items[0], items[2], f.readline())
    elif items[1] == "/":
        with open(pathpol, "r") as f:
            Division(items[0], items[2], f.readline())
    else:
        if items[2] == "-1":
            with open(pathpol, "r") as f:
                Reverse(items[0], f.readline())
        else:
            with open(pathpol, "r") as f:
                Exponentiation(items[0], items[2], f.readline())


with open(pathin, "r") as f:
    Calculate(f.readline())