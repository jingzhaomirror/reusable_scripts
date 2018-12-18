# ---
# import typical preprocessing, pipeline and model_selection modules
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.pipeline import Pipeline

# --- 
# import classification models and metrics
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import accuracy_score, f1_score, roc_auc_score

# ---
# convert categorical columns to dummy variables
X = pd.get_dummies(X, drop_first=True)

# ---
# train test split
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42) # user stratify=y for classification problem with inbalanced class

# --- 
# initiate the score table and define function for logging performance for classification problem
index = ['LogisticRegression','SVC','RandomForestClassifier','GradientBoostingClassifier'] # for classification problem
score_table = pd.DataFrame(index = index, columns= ['accuracy_score_train','f1_score_train','auc_train','accuracy_score_test','f1_score_test','auc_test'])

# ---
# define function for logging the results
def compute_log_result(algo, pred_train, pred_test):
    """compute and log the performance into the score_table for both training and test sets"""
    
    # compute the performance
    accuracy_train = accuracy_score(y_train, pred_train)
    accuracy_test = accuracy_score(y_test, pred_test)
    f1_train = f1_score(y_train, pred_train)
    f1_test = f1_score(y_test, pred_test)
    auc_train = roc_auc_score(y_train, pred_train)
    auc_test = roc_auc_score(y_test, pred_test)
    
    # log the performance
    score_table.loc[algo,:] = accuracy_train, f1_train, auc_train, accuracy_test, f1_test, auc_test
    
# ---
# fit logistic regression model with default parameters
logit = Pipeline([('scaler', StandardScaler()),('logit',LogisticRegression())])
logit.fit(X_train, y_train)
pred_train = logit.predict(X_train)
pred_test = logit.predict(X_test)
# print features and their coefficients based on the fitted logistic regression model
feature_coef = pd.DataFrame({'feature':X_train.columns, 'coefficient':logit.named_steps.logit.coef_[0]})
print(feature_coef.sort_values('coefficient',ascending=False))
# logging of model performance
compute_log_result("LogisticRegression", pred_train, pred_test)

# ---
# print the performance report for all prototyped algorithms
print(score_table)
