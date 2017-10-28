import os

from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import load_iris
from sklearn.externals import joblib

from sklearn.metrics import accuracy_score
from sklearn.externals import joblib
from sklearn.metrics import recall_score
from sklearn.metrics import precision_score
from sklearn.metrics import confusion_matrix


from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.learning_curve import learning_curve
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix
from sklearn.metrics import precision_recall_curve
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.ensemble import GradientBoostingClassifier

import pandas as pd
import numpy as np

# gensim
from gensim import corpora, models, similarities, matutils
# sklearn
from sklearn import datasets
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.cross_validation import train_test_split
from sklearn.cluster import KMeans
from sklearn.neighbors import KNeighborsClassifier
import sklearn.metrics.pairwise as smp

from sklearn.decomposition import NMF

#
# if __name__ == "__main__":
#         # Load Iris Data
#         iris_data = load_iris()
#         features = iris_data.data
#         feature_names = iris_data.feature_names
#         target = iris_data.target
#         target_names = iris_data.target_names
#
#         knn = KNeighborsClassifier(n_neighbors=3)  # replace with your own ML model here
#         knn.fit(features, target)
#
#         joblib.dump(knn, 'models/iris_model.pkl')
