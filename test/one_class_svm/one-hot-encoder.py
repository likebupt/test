import scipy
import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder
from sklearn.linear_model import LogisticRegression
# prepare sample dataset
n_samples = 100
n_cat_features = 15
cat_feature_names = [f'cat_feature_{i}' for i in range(n_cat_features)]
cat_features = np.random.choice(['a', 'b', 'c', 'd'], (n_samples, n_cat_features))
data_x = pd.DataFrame(cat_features, columns=cat_feature_names)
data_y = np.random.choice(['0', '1'], n_samples)
# prepare feature encoders
cat_feature_encoders = [OneHotEncoder().fit(cat_features[:, i].reshape(-1, 1)) for i in range(n_cat_features)]
# fit binary classification model
encoded_cat_features = [cat_feature_encoders[i].transform(cat_features[:, i].reshape(-1, 1)) for i in
                        range(n_cat_features)]
encoded_cat_features = scipy.sparse.hstack(encoded_cat_features, format='csr')
model = LogisticRegression(random_state=42).fit(encoded_cat_features, data_y)