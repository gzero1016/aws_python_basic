# 넘파이(Numpy)
# 고성능(대량) 수치 계산을 위한 라이브러리
# 벡터, 행렬 연산

import numpy as np

numArray1 = [1, 2, 3, 4, 5]
numArray2 = [6, 7, 8, 9, 10]

numArray3 = []
for i in range(len(numArray1)):
    numArray3.append(numArray1[i] + numArray2[i])

print(numArray3)

# np 를 사용하면 for문을 돌려 index 끼리 + 하지 않아도 편하게 + 할 수 있음
npArray1 = np.array(numArray1)
npArray2 = np.array(numArray2)
npArray3 = npArray1 + npArray2

print(npArray1)
print(npArray2)
print(npArray3)

npDoubleArray1 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
npDoubleArray2 = np.array([[11, 12, 13, 14, 15], [16, 17, 18, 19, 20]])

print(npDoubleArray1)
print(npDoubleArray2)
print(npDoubleArray1 + npDoubleArray2)

print(npArray1.shape)
print(npDoubleArray1.shape)

npArray4 = np.arange(10)    # 0 ~ 9 까지 10개의 리스트를 만들어줌
print(npArray4)

npArray5 = np.zeros(10) # 0으로 채워준다.
print(npArray5)

npArray6 = np.zeros_like(npDoubleArray1)    # npDoubleArray1 형태로 0으로 채워서 만들어라
print(npArray6)

npArray7 = np.ones(10)  # 1로 채워줌
print(npArray7)

npArray8 = np.ones_like(npDoubleArray1) # npDoubleArray1 형태로 1으로 채워서 만들어라
print(npArray8)

npArray9 = np.full((5, 3), 5)   # 10행 2열로 5를 다 채워준다.((행,열) , 원하는숫자)
print(npArray9)

npArray10 = np.full_like(npDoubleArray1, 5) # npDoubleArray1 형태로 5로 채워서 만들어라
print(npArray10)

print(npArray9 * 2)