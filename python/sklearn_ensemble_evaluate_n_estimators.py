# coding: utf-8

# This notebook shows, how to compute RandomForest's accuracy scores for different numbers of n_estimators without retraining the model
# the idea is to train RF with a large number of trees(n_estimators), then investigate the results on each fitted tree. 
# code snippet based on Jupyter notebook environment
# credit: coursera course: How to Win a Data Science Competition: Learn from Top Kagglers
# link to the notebook: https://acsyzihfdanercoyurekag.coursera-apps.org/notebooks/Reading%20materials/Hyperparameters_tuning_video2_RF_n_estimators.ipynb#

# load built-in dataset
import sklearn.datasets
from sklearn.model_selection import train_test_split

X, y = sklearn.datasets.load_digits(10,True)
X_train, X_val, y_train, y_val = train_test_split(X, y)

# import modules
import numpy as np
import matplotlib.pyplot as plt
% matplotlib inline
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# **Step 1:** train with a large number of estimators, n_estimators = 500 here
rf = RandomForestClassifier(n_estimators=500, max_depth=4, n_jobs=-1)
rf.fit(X_train, y_train)

# **Step 2:** Get predictions for each tree in Random Forest separately.
predictions = []
for tree in rf.estimators_:
    predictions.append(tree.predict_proba(X_val)[None, :])

# **Step 3:** Concatenate the predictions to a tensor of size `(number of trees, number of objects, number of classes)`.
predictions = np.vstack(predictions)

# **Step 4:** Сompute cumulative average of the predictions. That will be a tensor, that will contain predictions of the random forests for each `n_estimators`.
cum_mean = np.cumsum(predictions, axis=0)/np.arange(1, predictions.shape[0] + 1)[:, None, None]

# **Step 5:** Get accuracy scores for each `n_estimators` value
scores = []
for pred in cum_mean:
    scores.append(accuracy_score(y_val, np.argmax(pred, axis=1)))

# **That is it!** Plot the resulting scores to obtain similar plot to one that appeared on the slides.
plt.figure(figsize=(10, 6))
plt.plot(scores, linewidth=3)
plt.xlabel('num_trees')
plt.ylabel('accuracy');

# The plot shows that 150 trees are already sufficient to have stable result.
