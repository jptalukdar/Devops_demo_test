def add(*args):
    sum = 0
    for arg in args:
        if type(arg) == str:
            try:
                arg=float(arg)
            except :
                continue
        sum += arg

    return sum

