import pandas as pd
import numpy as np

###################################[ Series ]###################################

a = pd.Series({"a": 1, "b":2, "c":3})
print(a)
print(a.index.values)

print()

a = np.array([1, 2, 3, 4])
b = pd.Series(a)
print(b)

print()

print(b.index.values)

print()
###################################[ DataFrame ]###################################

a = {"a":[1, 2, 3, 0], "b":[4, 5, 6, 0], "c":[7, 8, 9, 0], "d":[10, 11, 12, 0]}
b = pd.Series(a)
c = pd.DataFrame(a, index=a.keys()) # a의 키값들을 index로 잡으면 자동으로 알아서 증가함
print(b)
print(c)

print()

print(c.index.values)   # 인덱스의 값 (행)
print(c.columns.values) # 컬럼의 값 (열)

print()

# 행이 맞지않는 부분은 자동으로 기존에 있던 값으로 채워넣는다. (자동으로 채워는주지만 값이 1개여야함)
a = pd.DataFrame({"a":(1,2,3), "b":1, "c":3})
print(a)

print()

a.index=["x", "y", "z"]
a.columns=["i","j","k"]
print(a)

print()

# loc = location
# iloc = index_location
print(a.loc[a["j"] == 1])   # 컬럼(열)의 값으로 조회 (조건도 넣을 수 있음)

print()

print(a.iloc[0])    # 인덱스번호로 조회(행)

print()

a = {"a":[1, 2, 3], "b":[4, 5, 6], "c":[7, 8, 9], "d":[10, 11, 12]}
b = pd.DataFrame(a)
print(b.describe())

print()

print(b.sum())  # 컬럼끼리 덧셈(열)

print()

print(b.sum(axis=1))    # 인덱스끼리 덧셈(행)

print()

print(b.min())  # 컬럼끼리 최소값(열)

print()

print(b.min(axis=1))    # 인덱스끼리 최소값(행)

print()

print(b.max())  # 컬럼끼리 최대값(열)

print()

print(b.max(axis=1))    # 인덱스끼리 최대값(행)

print()

print(b.mean()) # 컬럼끼리 평균(열)

print()

print(b.mean(axis=1))    # 인덱스끼리 평균(행)

print()

print(b.std(), b.var()) # std: 표준편차(열)     var: 분산(열)

print()

print(b.std(axis=1), b.var(axis=1)) # std: 표준편차(행)     var: 분산(행)