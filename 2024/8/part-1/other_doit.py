import copy
class A:
    def __init__(__self__, a,b):
        __self__.a = a
        __self__.b = b




a = A(1,1)
a.a = a
b = a
c = copy.deepcopy(a)
#a.a=2
print("b.a : ", b.a );
print("b.b : ", b.b );


print("c.a : ", c.a );
print("c.b : ", c.b );

print("a : ", a );
print("b : ", b );
print("c : ", c );
