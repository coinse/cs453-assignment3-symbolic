def half_square(x):
    if x % 2 == 0: 
        return x * x
    else:
        return x * 2

def compute(a, b):
    if b % 2 == 1:
        c = a + b + 1
        d = half_square(c)
        if 100 < d and d < 200:
            print("aha")
        else:
            print("huh?")
    else:
        e = half_square(a)
        if e < 0:
            print("yeah!")
        else:
            print("oh!")
    