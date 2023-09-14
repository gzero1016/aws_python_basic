import matplotlib.pyplot as plt
import numpy as np

x = [1, 2, 3, 4]
y = [2, 3, 4, 5]
# 그래프
plt.plot(x, y)
plt.show()

# 막대그래프
plt.bar(x, y)
plt.show()

# 꺽은선 그래프
# figure: 그래프의 틀
# add_subplot: 틀안에있는 그래프
figure = plt.figure()
axes = figure.add_subplot(111)

x2 = np.array(x)
y2 = np.array([4, 1, 3, 6])

axes.plot(x,y, color="red", linestyle="dashed", marker="^")
axes.plot(x2,y2, color="k", linestyle="dotted", marker="o")

plt.show()

# 꺽은선 그래프 두개로 나누기
figure = plt.figure()
axes1 = figure.add_subplot(121) # 1행 2열에서 1열
axes1.plot(x,y)

axes2 = figure.add_subplot(122) # 1행 2열에서 2열
axes2.plot(x2,y2)

plt.show()

