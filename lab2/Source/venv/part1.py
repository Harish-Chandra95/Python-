from sklearn.naive_bayes import GaussianNB
from sklearn import datasets, metrics
from sklearn.model_selection import train_test_split
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd


daibetesdataset=datasets.load_diabetes()
X=daibetesdataset.data
Y=daibetesdataset.target

model = GaussianNB()
model.fit(daibetesdataset.data, daibetesdataset.target)

X_train, X_test, Y_train, Y_test = train_test_split(daibetesdataset.data, daibetesdataset.target, test_size=0.4, random_state=1)

# Training the Model on Training Set
model.fit(X_train, Y_train)

# Training the Model on Testing Set
Y_predicted = model.predict(X_test)

# Evaluating the Model based on Testing Part
print("Gaussian Model Accuracy is ", metrics.accuracy_score(Y_test, Y_predicted) * 100)

#plotting each category

# https://seaborn.pydata.org/tutorial/categorical.html

#categories in dataset= age,sex,bmi,bp,s1,s2,s3,s4,s5,s6,y
#https://www4.stat.ncsu.edu/~boos/var.select/diabetes.html
diabetesdata = pd.read_table('E:\diabetes.txt')

plot = plt.figure(figsize=(8, 4))
plot.add_subplot(1, 1, 1)
cat = sns.countplot(diabetesdata['AGE'], label="Count") #using seaborn library
cat.set_xticklabels(cat.get_xticklabels(), rotation=40, ha="left", fontsize=8)
plt.tight_layout()
plt.show()

cat = sns.countplot(diabetesdata['SEX'], label="Count")
cat.set_xticklabels(cat.get_xticklabels(), rotation=40, ha="left", fontsize=6)
plt.tight_layout()
plt.show()

cat = sns.countplot(diabetesdata['BMI'], label="Count")
cat.set_xticklabels(cat.get_xticklabels(), rotation=40, ha="right", fontsize=6)
plt.tight_layout()
plt.show()

cat = sns.countplot(diabetesdata['BP'], label="Count")
cat.set_xticklabels(cat.get_xticklabels(), rotation=40, ha="right", fontsize=6)
plt.tight_layout()
plt.show()

cat = sns.countplot(diabetesdata['S1'], label="Count")
cat.set_xticklabels(cat.get_xticklabels(), rotation=40, ha="right", fontsize=6)
plt.tight_layout()
plt.show()

cat = sns.countplot(diabetesdata['S2'], label="Count")
cat.set_xticklabels(cat.get_xticklabels(), rotation=40, ha="right", fontsize=6)
plt.tight_layout()
plt.show()

cat = sns.countplot(diabetesdata['S3'], label="Count")
cat.set_xticklabels(cat.get_xticklabels(), rotation=40, ha="right", fontsize=6)
plt.tight_layout()
plt.show()

cat = sns.countplot(diabetesdata['S4'], label="Count")
cat.set_xticklabels(cat.get_xticklabels(), rotation=40, ha="right", fontsize=6)
plt.tight_layout()
plt.show()

cat = sns.countplot(diabetesdata['S5'], label="Count")
cat.set_xticklabels(cat.get_xticklabels(), rotation=40, ha="right", fontsize=6)
plt.tight_layout()
plt.show()

cat = sns.countplot(diabetesdata['S6'], label="Count")
cat.set_xticklabels(cat.get_xticklabels(), rotation=40, ha="right", fontsize=6)
plt.tight_layout()
plt.show()

cat = sns.countplot(diabetesdata['Y'], label="Count")
cat.set_xticklabels(cat.get_xticklabels(), rotation=40, ha="right", fontsize=6)
plt.tight_layout()
plt.show()