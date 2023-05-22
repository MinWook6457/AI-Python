## 'plot_confusion_matrix' from 'sklearn.metrics' 오류 발생
## 해결중

import matplotlib.pyplot as plt

from sklearn import datasets, metrics
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

digits = datasets.load_digits()
n_samples = len(digits.images)
data = digits.images.reshape((n_samples,-1))


knn = KNeighborsClassifier(n_neighbors=6)

X_train, X_test, y_train, y_test = train_test_split(data,digits.target,test_size=0.2)

knn.fit(X_train,y_train)
y_pred = knn.predict(X_test)

disp = metrics.plot_confusion_matrix(knn,X_test,y_test)
plt.show()