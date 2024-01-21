def bar(x, y, z):
    if x < y:
        if z < y:
            if x < z:
                result = z
            else:
                result = x
        else:
            result = y
    else:
        result = 0;