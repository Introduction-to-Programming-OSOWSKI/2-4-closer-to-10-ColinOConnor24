def close10(x, y):
    a = 10 - x
    b = 10 - y
    a = abs(a)
    b = abs(b)
    if a == b:
        return 0
    elif a < b:
        return x
    else:
        return y