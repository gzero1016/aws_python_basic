x = list(map(int, input("X : ")))
y = list(map(int, input("y : ")))

x.reverse()
y.reverse()

result = 0
i = 0

for numY in y:
    j = 0
    subResult = 0

    for numX in x:
        subResult += numX * numY * (10 ** j)
        j += 1

    print(subResult)
    result += subResult * (10 ** i)
    i += 1
print(result)