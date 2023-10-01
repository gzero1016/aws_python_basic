for num in [1,2,3,4,5]:
    print(num)

print()

for num in range(1, 101):
    print(num)

print()

for i in range(2, 10):
    for j in range(1, 10):
        print(f"{i} * {j} = {i*j}", end="\t")
    print(f"{i} * {j} = {i*j}")

print()

for j in range(1, 10):
    for i in range(2, 10):
        print(f"{i} * {j} = {i*j}", end="\t")
    print(f"{i} * {j} = {i*j}")