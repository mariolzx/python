X = 11                       # Global in module

def g1():
    print(X)                 # Reference global in module

def g2():
    global X
    X = 22                   # Change global in module

def h1():
    X = 33                   # Local in function
    def nested():
        print(X)             # Reference local in enclosing scope

def h2():
    X = 33                   # Local in function
    def nested():
        nonlocal X           # Python 3.0 statement
        X = 44               # Change local in enclosing scope
