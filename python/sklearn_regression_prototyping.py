# ---
# import typical preprocessing, pipeline and model_selection modules
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline

# ---
# import regression models and metrics
from sklearn.linear_model import Lasso
from sklearn.linear_model import Ridge
from sklearn.svm import SVR
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import GradientBoostingRegressor 
from sklearn.metrics import r2_score, mean_squared_error 

# ---
# convert categorical columns to dummy variables
X = pd.get_dummies(X, drop_first=True)

# ---
# train test split
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42) # user stratify=y for classification problem with inbalanced class

# --- 
# initiate the score table and define function for logging performance for regression problem
index = ['Lasso','Ridge','SVR','RandomForestRegressor','GradientBoostingRegressor']
score_table = pd.DataFrame(index = index, columns= ['r2_train','mse_train','rmse_train','r2_test','mse_test','rmse_test'])

# ---
# define function for logging the results
def compute_log_result(algo, pred_train, pred_test):
    """compute and log the performance into the score_table for both training and test sets"""
    
    # compute the performance
    r2_train = accuracy_score(y_train, pred_train)
    r2_test = accuracy_score(y_test, pred_test)
    mse_train = f1_score(y_train, pred_train)
    mse_test = f1_score(y_test, pred_test)
    rmse_train = np.sqrt(mse_train)
    rmse_test = np.sqrt(rmse_test)
    
    # log the performance
    score_table.loc[algo,:] = r2_train, mse_train, rmse_train, r2_test, mse_test, rmse_test
    
# ---
# fit Lasso regression model with default parameters
lasso = Pipeline([('scaler', StandardScaler()),('lasso',Lasso())])
lasso.fit(X_train, y_train)
pred_train = lasso.predict(X_train)
pred_test = lasso.predict(X_test)
# print features and their coefficients based on the fitted logistic regression model
feature_coef = pd.DataFrame({'feature':X_train.columns, 'coefficient':lasso.named_steps.lasso.coef_[0]})
print(feature_coef.sort_values('coefficient',ascending=False))
# logging of model performance
compute_log_result("Lasso", pred_train, pred_test)

# fit Ridge regression model with default parameters
ridge = Pipeline([('scaler', StandardScaler()),('ridge',Ridge())])
ridge.fit(X_train, y_train)
pred_train = ridge.predict(X_train)
pred_test = ridge.predict(X_test)
# print features and their coefficients based on the fitted logistic regression model
feature_coef = pd.DataFrame({'feature':X_train.columns, 'coefficient':ridge.named_steps.ridge.coef_[0]})
print(feature_coef.sort_values('coefficient',ascending=False))
# logging of model performance
compute_log_result("Ridge", pred_train, pred_test)

# ---
# fit support vector machine regression model with default parameters
svr = Pipeline([('scaler', StandardScaler()),('svr', SVR())])
svr.fit(X_train, y_train)
pred_train = svr.predict(X_train)
pred_test = svr.predict(X_test)
# logging of model performance
compute_log_result("SVR", pred_train, pred_test)

# ---
# fit random forest regression model with default parameters
rfr = Pipeline([('scaler', StandardScaler()),('rfr', RandomForestRegressor())])
rfr.fit(X_train, y_train)
pred_train = rfr.predict(X_train)
pred_test = rfr.predict(X_test)
# print feature importance
feature_rank = pd.DataFrame({'feature': X_train.columns, 'importance': rfr.named_steps.rfr.feature_importances_})
print(feature_rank.sort_values(by='importance',ascending=False))
# logging of model performance
compute_log_result("RandomForestRegressor", pred_train, pred_test)

# ---
# fit gradient boosting regression model with default parameters
gbr = Pipeline([('scaler', StandardScaler()),('gbr', GradientBoostingRegressor())])
gbr.fit(X_train, y_train)
pred_train = gbr.predict(X_train)
pred_test = gbr.predict(X_test)
# print feature importance
feature_rank = pd.DataFrame({'feature': X_train.columns, 'importance': gbr.named_steps.gbr.feature_importances_})
print(feature_rank.sort_values(by='importance',ascending=False))
# logging of model performance
compute_log_result("GradientBoostingRegressor", pred_train, pred_test)

# ---
# print the performance report for all prototyped algorithms
print(score_table)
