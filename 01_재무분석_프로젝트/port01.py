#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
font_path = r'C:\WINDOWS\FONTS\MALGUNSL.TTF' # 폰트 경로
font_name = fm.FontProperties(fname=font_path).get_name()
plt.rc('font', family='Malgun Gothic')


# # 1. 재무제표 데이터 로드

# In[2]:


# 1. 재무제표 데이터 로드
df1 = pd.read_excel('삼성전자_재무제표.xlsx', engine='openpyxl',sheet_name='01재무상태표', index_col="계정")
df2 = pd.read_excel('삼성전자_재무제표.xlsx', engine='openpyxl',sheet_name='02손익계산서', index_col="계정")
df1_shifted = df1.shift(-1, axis=1)

자산 = df1.loc["자산총계"]
부채 = df1.loc["부채총계"]
자본 = df1.loc["자본총계"]

당기순이익 = df2.loc["당기순이익"]
전_자본 = df1_shifted.loc["자본총계"]
전_자산 = df1_shifted.loc["자산총계"]

유동자산 = df1.loc["유동자산"]
유동부채 = df1.loc["유동부채"]

당좌자산 = 유동자산 - df1.loc["재고자산 (주8)"]

매출액 = df2.loc["매출액 (주29)"]
영업이익 = df2.loc["영업이익 (주29)"]


# # 2. 주요 재무비율 계산

# In[3]:


# 2. 주요 재무비율 계산

# a) 부채비율
부채비율 = 부채 / 자본 * 100

# b) ROE
ROE = 당기순이익 / 전_자본 * 100

# c) ROA
ROA = 당기순이익 / 전_자산 * 100

# d) 유동비율
유동비율 = 유동자산 / 유동부채 * 100

# e) 당좌비율
당좌비율 = 당좌자산 / 유동부채 * 100

# f) 영업이익률
영업이익률 = 영업이익 / 매출액 * 100


# # 3. 결과 출력

# In[4]:


# 3. 결과 출력

formatted_부채비율 = 부채비율.map('{:.2f} %'.format)
print(formatted_부채비율)

결과 = pd.DataFrame({
    '자산': 자산,
    '부채': 부채,
    '자본': 자본,
    '당기순이익': 당기순이익,
    '부채비율(%)': 부채비율,
    'ROE': ROE,
    'ROA': ROA,
    '유동비율': 유동비율,
    '당좌비율': 당좌비율,
    '영업이익률': 영업이익률
})
print(결과)


결과_포맷 = 결과.style.format({
    '자산': '{:,.0f}',
    '부채': '{:,.0f}',
    '자본': '{:,.0f}',
    '당기순이익': '{:,.0f}',
    '부채비율(%)': '{:.2f}',
    'ROE': '{:.2f}',
    'ROA': '{:.2f}',
    '유동비율': '{:.2f}',
    '당좌비율': '{:.2f}',
    '영업이익률': '{:.2f}',
})
print(결과_포맷)


# # 4. 그래프 그리기

# In[5]:


# 4. 그래프 그리기
fig, axes = plt.subplots(2, 3, figsize=(15, 4))
axes = axes.flatten()

부채비율.plot(kind='bar', ax=axes[0], title='부채비율 추이')
ROE.plot(kind='bar', ax=axes[1], title='ROE 추이')
ROA.plot(kind='bar', ax=axes[2], title='ROA 추이')
유동비율.plot(kind='bar', ax=axes[3], title='유동비율 추이')
당좌비율.plot(kind='bar', ax=axes[4], title='당좌비율 추이')
영업이익률.plot(kind='bar', ax=axes[5], title='영업이익률 추이')


for ax in axes:
    # ax.tick_params를 사용하여 해당 서브플롯의 X축 틱(tick) 속성을 변경합니다.
    ax.tick_params(axis='x', rotation=0)

plt.tight_layout()
plt.show()
결과_포맷


# # 5. 분석 코멘트

# In[6]:


# 5. 분석 코멘트
print("\n=== 재무 분석 요약 ===")
print(f"평균 부채비율: {부채비율.mean():.2f}%")
print(f"평균 ROE: {ROE.mean():.2f}%")
print(f"평균 ROA: {ROA.mean():.2f}%")
print(f"평균 유동비율: {유동비율.mean():.2f}%")
print(f"평균 당좌비율: {당좌비율.mean():.2f}%")
print(f"평균 영업이익률: {영업이익률.mean():.2f}%")

if 부채비율.iloc[-1] > 200:
    print("⚠️ 부채비율 높음 (200% 초과)")
if ROE.iloc[-1] < 10:
    print("⚠️ ROE 낮음 (10% 미만)")
if 유동비율.iloc[-1] < 100:
    print("⚠️ 유동비율 낮음 (100% 미만)")
if 당좌비율.iloc[-1] < 100:
    print("⚠️ 당좌비율 낮음 (100% 미만")
if 영업이익률.iloc[-1] < 0:
    print("⚠️ 영업이익률 낮음 (0% 미만)")


# In[ ]:




