
def intcode(code):
    code = [int(x.strip()) for x in code.split(',')] + [0] * 100000

    i = 0
    mode = None
    base = 0

    def get_position(i, m):
        if m == 0:
            return code[i]
        if m == 1:
            return i
        if m == 2:
            return code[i] + base

    def get_params(count):
        ret =  [get_position(i + 1 + x, mode[x]) for x in range(count-1)]
        if len(ret) == 1: return ret[0]
        return ret

    def get_mode(op):
        o = op % 100
        C = (op % 1000)//100
        B = (op % 10000)//1000
        A = (op % 100000)//10000
        return (o, (C, B, A))

    while True:
        # print("i", i)
        op = code[i]
        op, mode = get_mode(op)
        # print("op", op)

        if op == 1:
            a, b, c = get_params(4)
            code[c] = code[a] + code[b]
            i += 4

        elif op == 2:
            a, b, c = get_params(4)
            code[c] = code[a] * code[b]
            i += 4

        elif op == 3:
            a = get_params(2)
            inp = yield
            code[a] = inp
            i += 2

        elif op == 4:
            a = get_params(2)
            out = code[a]
            yield out
            i += 2

        elif op == 5:
            a, b = get_params(3)
            # print(code[i])
            # print(a, b)
            if code[a] != 0:
                i = code[b]
            else:
                i += 3

        elif op == 6:
            a, b = get_params(3)
            if code[a] == 0:
                i = code[b]
            else:
                i += 3

        elif op == 7:
            a, b, c = get_params(4)
            if code[a] < code[b]:
                code[c] = 1
            else:
                code[c] = 0
            i += 4

        elif op == 8:
            a, b, c = get_params(4)
            if code[a] == code[b]:
                code[c] = 1
            else:
                code[c] = 0
            i += 4

        elif op == 9:
            a = get_params(2)
            base += code[a]
            i += 2

        elif op == 99:
            break


def repeat(f):
    def function(*args, **kwargs):
        try:
            while True:
                f(*args, **kwargs)
        except StopIteration:
            pass
    return function
