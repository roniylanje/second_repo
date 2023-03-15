#Implicit Type Conversion
x=10
y="hi"
z=x
x=10.09

print(type(x))
print(type(y))
print(type(z))
print(type(x))# it will overwrite the int data type

#Explicit Type Conversion
one='one junit'
w=set(one)
e=tuple(one)
print(e)
print(w)
r=list(one)
print(r)
u="1000111"
o=int(u,2)
print(o)