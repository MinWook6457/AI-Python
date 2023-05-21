import numpy as np
import matplotlib.pyplot as plt

X = np.array([0.0, 1.0 , 2.0])
y = np.array([3.0, 3.5 , 5.5])

w = 0 # 가중치
b = 0 # 바이어스

lrate = 0.01 # 학습률
epochs = 1000 # 반복 횟수

n = float(len(X)) # 입력 데이터 갯수

# 경사하강법
for i in range(epochs) :
    y_pred = w*X + b # 선형회귀 예측값
    dw = (2/n) * sum(X*(y_pred-y)) # 넘파이 배열 간의 산술 계산은 요소별로 적용
    db = (2/n) * sum(y_pred -y) # sum()은 모든 요소들의 합을 계산하는 내장 함수
    w = w - lrate * dw
    b = b - lrate * db

# 기울기와 절편 출력
print(w,b)

# 예측값 생성
y_pred = w*X + b

# 입력 데이터 그래프에 찍기
plt.scatter(X,y)

# 예측값은 선그래프로 그리기
plt.plot([min(X),max(X)], [min(y_pred),max(y_pred)],color = 'red')
plt.show()



