
import matplotlib.pyplot as plot
import numpy
from sklearn import datasets, linear_model, metrics
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split

# Loading diabetes Dataset
diabetesdataset = datasets.load_diabetes()

X = diabetesdataset.data
Y = diabetesdataset.target

# Training and Testing Data

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2,random_state = 21)

#Cross-Validation
#C = 1.0 --> SVM Regularization Parameter

#Poly Kernel

clf = SVC(kernel='poly',degree=4, C=1.0, gamma=0.1).fit(X_train, Y_train)
clf.fit(X_test, Y_test)
y_pred = clf.predict(X_test)
print(" Kernel Accuracy :", metrics.accuracy_score(Y_test, y_pred) *100)


#https://stackoverflow.com/questions/42191717/python-random-state-in-splitting-dataset/42197534
# Increasing Random State increases accuracy

#RBF Kernel


clf1 = SVC(kernel='rbf', C=1.0, gamma=0.2).fit(X_train, Y_train)
clf1.fit(X_test, Y_test)
y_pred = clf1.predict(X_test)
print("RBF kernel Accuracy : ",metrics.accuracy_score(Y_test, y_pred) *100)

# Plotting the data
plot.scatter(X[:, 0], X[:, 1], c=Y)
plot.show()