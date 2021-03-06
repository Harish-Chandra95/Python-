
from sklearn.svm import LinearSVC
from sklearn.datasets import load_iris
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from matplotlib import pyplot as plt
from sklearn import metrics


from sklearn.svm import SVC

iris = load_iris()

X = iris.data
Y = iris.target
X_train, X_test, Y_train, Y_test = train_test_split(X, Y,
                            test_size=0.80, random_state=0)

for Model in [GaussianNB, LinearSVC,SVC]:
    clf = Model().fit(X_train, Y_train)
    y_pred = clf.predict(X_test)
    print('%s: %s' %
          (Model.__name__, metrics.f1_score(Y_test, y_pred, average="macro")))













# import numpy as np
# import matplotlib.pyplot as plt
# from sklearn import svm, datasets
#
#
# def make_meshgrid(x, y, ):
#     """Create a mesh of points to plot in
#
#     Parameters
#     ----------
#     x: data to base x-axis meshgrid on
#     y: data to base y-axis meshgrid on
#     h: stepsize for meshgrid, optional
#
#     Returns
#     -------
#     xx, yy : ndarray
#     """
#     x_min, x_max = x.min() -1 , x.max() +1
#     y_min, y_max = y.min() -1, y.max() +1
#     xx, yy = np.meshgrid(np.arange(x_min, x_max, ),
#                          np.arange(y_min, y_max, ))
#     return xx, yy
#
#
# def plot_contours(ax, clf, xx, yy, **params):
#     """Plot the decision boundaries for a classifier.
#
#     Parameters
#     ----------
#     ax: matplotlib axes object
#     clf: a classifier
#     xx: meshgrid ndarray
#     yy: meshgrid ndarray
#     params: dictionary of params to pass to contourf, optional
#     """
#     Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
#     Z = Z.reshape(xx.shape)
#     out = ax.contourf(xx, yy, Z, **params)
#     return out
#
#
# # import some data to play with
# iris = datasets.load_iris()
# # Take the first two features. We could avoid this by using a two-dim dataset
# x = iris.data[:, :2]
# y = iris.target
#
# # we create an instance of SVM and fit out data. We do not scale our
# # data since we want to plot the support vectors
# C = 1.0  # SVM regularization parameter
# models = (
#           svm.LinearSVC(C=C),
#           svm.SVC(kernel='rbf', gamma=0.7, C=C),
#           )
# models = (clf.fit(x, y) for clf in models)
#
# # title for the plots
# titles = (
#           'LinearSVC (linear kernel)',
#           'SVC with RBF kernel',
#           )
#
# # Set-up 2x2 grid for plotting.
# fig, sub = plt.subplots(1,2)
# plt.subplots_adjust(wspace=0.4, hspace=0.4)
#
# X0, X1 = x[:, 0], x[:, 1]
# xx, yy = make_meshgrid(X0, X1)
#
# for clf, title, ax in zip(models, titles, sub.flatten()):
#     plot_contours(ax, clf, xx, yy,
#                   cmap=plt.cm.summer, alpha=0.8)
#     ax.scatter(X0, X1, c=y, cmap=plt.cm.summer, s=20, edgecolors='k')
#     ax.set_xlim(xx.min(), xx.max())
#     ax.set_ylim(yy.min(), yy.max())
#     ax.set_xlabel('Sepal length')
#     ax.set_ylabel('Sepal width')
#     ax.set_xticks(())
#     ax.set_yticks(())
#     ax.set_title(title)
#
# plt.show()