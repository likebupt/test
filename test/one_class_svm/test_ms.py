'''
Anomaly Detection.
'''
import numpy
import pandas
from microsoftml import rx_oneclass_svm, rx_predict
from revoscalepy.etl.RxDataStep import rx_data_step
from microsoftml.datasets.datasets import get_dataset

iris = get_dataset("iris")

import sklearn
if sklearn.__version__ < "0.18":
    from sklearn.cross_validation import train_test_split
else:
    from sklearn.model_selection import train_test_split

irisdf = iris.as_df()
data_train, data_test = train_test_split(irisdf)

# Estimate a One-Class SVM model
model = rx_oneclass_svm(
            formula= "~ Sepal_Length + Sepal_Width + Petal_Length + Petal_Width",
            data=data_train)

# Add additional non-iris data to the test data set
data_test["isIris"] = 1.0
not_iris = pandas.DataFrame(data=dict(Sepal_Length=[2.5, 2.6], 
        Sepal_Width=[.75, .9], Petal_Length=[2.5, 2.5], 
        Petal_Width=[.8, .7], Species=["not iris", "not iris"], 
        isIris=[0., 0.]))

merged_test = pandas.concat([data_test, not_iris])

scoresdf = rx_predict(model, data=merged_test, extra_vars_to_write=["isIris"])

# Look at the last few observations
print(scoresdf.tail())