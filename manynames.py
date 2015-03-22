X=11

def f():
    print(X)

def g():
    X=22
    print(X)

class C:
     X = 33                    # Class attribute (C.X)
     def m(self):
         X = 44                # Local variable in method (X)
         self.X = 55           # Instance attribute (instance.X)


#c1=C()
#c1.X
#c1.m()
#c1.X
#C.m(c1)
#c1.X


if __name__=='__main__':
    print(X)
    f()
    g()
    print(X)

    obj=C()
    print(obj.X)

    obj.m()        #attach attribute name X to instance now
    print(obj.X)   #55:instance
    print(C.X)     #33:class(Also known as: obj.X if no X in instance)

    #print(C.m.X)  #Fails:only visible in method
    #pirnt(g.X)    #Fails: only visible in function
    
