x={"a","b","c"}
y=(1,2,3)
z=[4,5,2]
print(type(x));
print(type(y));
print(type(z));
x.add("d")
print(x)
z.append(5)
print(y)
print(z)
for i in x:
   print (i)
if 5 in z:
    print("yes")
x.remove("b")
print(x)
z.remove(4)
print(z)
z.insert(1,7)
print(z)
z.extend(y)
print(z)
print(z.count(2))
del y
print(y)


   

