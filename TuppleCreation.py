#Creation of tupple
tup1=(1,2,3)
tup2=('abc','def','ght')
tup3=('uyt',12.1,4)
tup4=(tup1,tup2,tup3)
print(tup4)
tup5=(tup4,['tt','uuu'])
print(tup5)
Tuple1 = ('Geeks','ttt') * 3
print(Tuple1)
#unpacking tuple
a,b,c,d,e,r=Tuple1
print(a)
print(b)
print(c)
print(d)
print(e)
print(r)
T1=('awe','kiu')
T2=('iuu','wwsd')
T3=T1+T2
print(T3)
Tuple4 = tuple('GEEKSFORGEEKS')
print("First item removal")
print(Tuple4[::-1])
print(Tuple4[:1])
print(Tuple4[1:])
print(Tuple4[::1])
name='snehal'
t6=tuple(name)
print(t6[::-1])
#We can't delete tuple
Tuple8 = (0, 1, 2, 3, 4)
del Tuple8

print(Tuple8)
tuple11=(1,1,1,2,3,3,3,4)
set1=list(tuple11)
print(set1)



