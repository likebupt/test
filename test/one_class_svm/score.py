from sklearn.externals import joblib

# restore
svm_score = joblib.load('one-class-svm.pkl')
print(svm_score.predict(X[0:1]))#预测第一个X

x = test['x1'] 
y = test['x2'] 
y_pred = svm.predict(test[['x1','x4','x5']]) 
colors = np.array(['#377eb8', '#ff7f00']) 
plt.scatter(x, y, alpha=0.7, c=colors[(y_pred + 1) // 2]) plt.xlabel('x1') 
plt.ylabel('x4')