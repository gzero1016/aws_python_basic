import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("202108_202308_주민등록인구및세대현황_월간.csv", encoding="cp949")
print(data.columns)
print()
print(data.index)
print()
print(data)

# 연도별 행정구역별 거주자 인구
print("---------------------------------------------")
print(data.iloc[1, 0])  # 부전제1동
# 열번호, range(index 1번부터 컬럼의수 만큼 가져올건데 6씩 증가시켜서 가져옴)
print(data.iloc[1, range(1, len(data.columns), 6)]) # 총인구수

# 가야제1동 세대당 인구수
print("---------------------------------------------")
print(f"""
{data.iloc[data.query('행정구역.str.contains("가야제1동")').index.values[0], 0]}
""")
rowIndex = data.query('행정구역.str.contains("가야제1동")').index.values[0]
print(data.iloc[rowIndex, range(3, len(data.columns),6)])

data.plot.bar()