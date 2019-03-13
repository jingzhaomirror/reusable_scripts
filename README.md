# Reusable Scripts

## 'Python' folder: 
1. df_pivot_sparse_matrix.py:
pivot pandas dataframe into a **sparse matrix** directly. Unlike Pandas pivot function, work well with big matrix of high sparsity. 

2. rank_metrics.py:
A list of functions for computing recommendation rank effectiveness. Metrics include: 
binary: mean_reciprocal_rank, precision_at_k, r_precision, average_precision, mean_average_precision
multivalues or binary: dcg_at_k, ndcg_at_k

3. sklearn_classification_prototyping.py:
Reusable codes for prototyping off-the-shelf classification algorithms, including LogisticRegression, SVC, RandomForestClassifier, GradientBoostingClassifier. Evaluation metrics include accuracy_score, f1_score, roc_auc_score. 

4. sklearn_regression_prototyping.py:
Reusable codes for prototyping off-the-shelf Regression algorithms, including Lasso, Ridge, SVR, RandomForestRegressor, GradientBoostingRegressor. Evaluation metrics include r2_score, mean_squared_error, RMSE. 

5. sklearn_ensemble_evaluate_n_estimators.py:
code example for computing RandomForest's accuracy scores for different numbers of n_estimators without retraining with individual models/grid search

6. bokeh_interactive_visual.py:
Reusable codes for creating interactive visualization based on Bokeh server. 
