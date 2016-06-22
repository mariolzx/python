X=1

def nester():
    X=2
    print(X)
    class C:
        X=3
        print(X)
        def method1(self):
            print("Inside method1: %d" %X)
            print("self.X: %d" %self.X)
        def method2(self):
            X=4
            print(X)
            self.X=5
            print(self.X)
    I=C()
    I.method1()
    I.method2()

print(X)
nester()
print('-'*40)

#simple names never search enclosing class statements--
#just defs, modules, and built-ins
