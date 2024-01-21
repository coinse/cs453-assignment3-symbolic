def foo(x):
    if x * 32 - 16 == 4:
        return True
    else:
        return False

def bar(x, y):
    if foo(y) and x < 32:
        print("Arrrgh!")
    elif not foo(x) and (y == 32 or x + y == 100):
        print("Huh??")
    else:
        print("Nevermind.")