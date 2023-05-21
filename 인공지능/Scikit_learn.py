import matplotlib.pyplot as plt 
from sklearn import linear_model

reg = linear_model.LinearRegression() # 선형 회귀 모델 생성

X = [[30],[35],[20],[15],[3]] # 2차원 행열임
y = [90,95,70,40,10]

reg.fit(X,y) # 학습

print(reg.predict([[40]]))


# 학습 데이터와 y값의 산포도를 그림
plt.scatter(X,y,color='black')

# 학습 데이터를 입력으로 하여 예측값을 계산
y_pred = reg.predict(X)

plt.plot(X,y_pred,color='blue',linewidth=3)
plt.show()