# Classify data
# https://pythonbasics.org/machine-learning-classifier/

from sklearn import tree

features = [[0,50],[0,60],[1,35],[1,36],[1,40]]
labels = [0,0,1,1,1]

algorithm = tree.DecisionTreeClassifier()
algorithm = algorithm.fit(features, labels)

newData = [[0,51]]
print(algorithm.predict(newData))
