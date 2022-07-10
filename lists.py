#Lists

impares = [i**2 for i in range(100) if i%2 != 0]
#print(impares)

a,b,c = impares[:3]
#print(a,b,c)


# id a == id b

a = [1,2,3]
b = a

print(a,b)
print(id(a), "<- a")
print(id(b), "<- b")

a[1] = "a"
print(a,b)

# id a != id b

a = [1,2,3]
b = list(a)
print(id(a), "<- a")
print(id(b), "<- b")






