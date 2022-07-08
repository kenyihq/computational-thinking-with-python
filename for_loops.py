# For loops

fruits = ["apple", "banana", "pear"]

for i in fruits:
    print(i)

loops = iter(fruits)

print(next(loops)) # apple
print(next(loops)) # banana
print(next(loops)) # pear
print(next(loops)) # StopInteration