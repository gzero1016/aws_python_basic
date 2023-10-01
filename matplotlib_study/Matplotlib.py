import matplotlib.pyplot as plt
import numpy as np
from matplotlib import font_manager, rc

x = [1, 2, 3, 4]
y = [2, 3, 4, 5]
# 그래프
plt.plot(x, y)
plt.show()

# 막대그래프 bar
plt.bar(x, y)
plt.show()

# 꺽은선 그래프 plot
# figure: 그래프의 틀
# add_subplot: 틀안에있는 그래프
figure = plt.figure()
axes = figure.add_subplot(111)

x2 = np.array(x)
y2 = np.array([4, 1, 3, 6])

axes.plot(x,y, color="red", linestyle="dashed", marker="^")
axes.plot(x2,y2, color="k", linestyle="dotted", marker="o")

plt.show()

x3 = np.array([1, 2, 6, 4])
y3 = np.array([1, 2, 6, 3])

x4 = np.array([6, 1, 3, 4])
y4 = np.array([1, 6, 3, 6])

# 꺽은선 그래프 여러개로 나누기
figure = plt.figure()
axes1 = figure.add_subplot(221) # 2행 2열에서 1번째
axes1.plot(x,y)

axes2 = figure.add_subplot(222) # 2행 2열에서 2번째
axes2.plot(x2,y2)

axes3 = figure.add_subplot(223) # 2행 2열에서 3번째
axes3.plot(x3,y3)

axes4 = figure.add_subplot(224) # 2행 2열에서 4번째
axes4.plot(x4,y4)

plt.show()

# 중첩 막대그래프
figure = plt.figure()
axes = figure.add_subplot(111)

axes.bar(x, y)
axes.bar(x2, y2)
plt.show()

# 꺽은선 그래프와 막대그래프 같이 시각화 시키기
figure = plt.figure()
axes1 = figure.add_subplot(111)
axes2 = axes1.twinx()

axes1.bar(x, y, color="blue", label="bar")
axes2.plot(x2, y2, color="red", label="plot")
plt.show()


# 점그래프 scatter
rc("font", family="AppleGothic")

figure = plt.figure()
axes = figure.add_subplot(111)

x = [1, 2, 3, 4]
y = [2, 4, 6, 8]
x2 = [1, 1, 3, 4]
y2 = [6, 2, 4, 6]

axes.scatter(x,y)
axes.scatter(x2,y2)
plt.title("제목")
plt.xlabel("엑스축 이름")
plt.ylabel("와이축 이름")
plt.show()

# 원형그래프

# 폰트 찾기
# font_list = font_manager.findSystemFonts(fontpaths=None, fontext="ttf")
# for font in font_list:
#     if font.find("Gothic") != -1:
#         print(font)

rc("font", family="AppleGothic")

figure = plt.figure()
axes = figure.add_subplot(111)

label = ["축구", "농구", "야구", "배구"]
data = [10, 20, 5, 30]

axes.pie(data, labels=label)
# plt.show()
plt.savefig("test")