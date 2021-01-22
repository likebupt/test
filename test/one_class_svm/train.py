import pandas as pd
from sklearn.svm import OneClassSVM 
import joblib

# set input parameters
data_path = 'credit_card.csv'
nu_value = 0.1
tolerance_value = 0.0001
label_col = 'Col21'

# read input data
input_df = pd.DataFrame([]) 
input_df = pd.read_csv(data_path)

# train model 
X_train = input_df.loc[:, input_df.columns != label_col]
Y_train = input_df[label_col]

svm = OneClassSVM(kernel='rbf', nu=nu_value, tol=tolerance_value) 
svm.fit(X_train)

# Save
joblib.dump(svm, 'one-class-svm.pkl')
