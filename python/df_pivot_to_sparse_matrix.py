# define method for pivoting dataframe into a sparse matrix directly
# version: python 3.6.5, pandas 0.23.3, numpy 1.15.0 scipy 1.1.0

from scipy.sparse import csr_matrix
from pandas.api.types import CategoricalDtype

# return the resulting sparse matrix only
def df_pivot_sparse_matrix_simple(df, idx, col, val):
    """pivot a pandas dataframe into sparse matrix directly using scipy.sparse.csr_matrix and return the resulting sparse matrix. 
    necessary when the df is large and pandas pivot (dense matrix) doesn't work due to space (memory) constrain. 
    ---
    input
    df: the pandas dataframe of interest
    idx: the column name of the df to be used as the index in the sparse matrix;
    col: the column name of the df to be used as the column in the sparse matrix;
    val: the column name of the df to be used as the actual value in the sparse matrix;
    ---
    note: there should be only one unique value of each idx, col combination
    """
    x = df[idx].astype(CategoricalDtype(ordered=True)).cat.codes
    y = df[col].astype(CategoricalDtype(ordered=True)).cat.codes
    return csr_matrix((df[val].values, (x, y)), shape=(df[idx].nunique(), df[col].nunique()))


# return the resulting sparse matrix along with the mapping dictionaries of matrix indices to the orignial values in the corresponding columns of df
def df_pivot_sparse_matrix(df, idx, col, val):
    """pivot a pandas dataframe into sparse matrix directly using scipy.sparse.csr_matrix and return the resulting sparse matrix, 
    necessary when the df is large and pandas pivot (dense matrix) doesn't work due to space (memory) constrain. 
    ---
    input
    df: the pandas dataframe of interest
    idx: the column name of the df to be used as the index in the sparse matrix;
    col: the column name of the df to be used as the column in the sparse matrix;
    val: the column name of the df to be used as the actual value in the sparse matrix;
    ---
    return:
    sparse_matrix: the resulting sparse matrix
    map_idx: the dictionary to map the unique values in the idx column of the original df to the numerical row indices of the sparse matrix 
    map_col: the dictionary to map the uniqe values in the col column of the original df to the numerical column indices of the sparse matrix 
    ---
    note: there should be only one unique value of each idx, col combination
    """
    idx_c = CategoricalDtype(sorted(df[idx].unique()),ordered=True) # find unique values in the idx column and define as a categorical type
    col_c = CategoricalDtype(sorted(df[col].unique()),ordered=True) # find unique values in the col column and define as a categorical type

    x = df[idx].astype(idx_c).cat.codes # cast columns to the newly created categorical type and access the underlying integer codes (corresponding numbering of the categories)
    y = df[col].astype(col_c).cat.codes 
    sparse_matrix = csr_matrix((df[val].values, (x, y)), \
                           shape=(len(idx_c.categories), len(col_c.categories))) # map to the sparse matrix
    
    map_idx = dict(zip(list(idx_c.categories),np.arange(len(idx_c.categories)))) # create the mapping dictionaries
    map_col = dict(zip(list(col_c.categories),np.arange(len(col_c.categories))))
                               
    return sparse_matrix, map_idx, map_col
