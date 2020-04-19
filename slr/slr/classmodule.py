import pandas as pd
from sklearn.model_selection import  train_test_split
from sklearn.linear_model import LinearRegression

class MyClass():
    def __init__(self, arg):
        self.arg = arg
    def Regression(self):
    	ar = self.arg[0]
    	file = self.arg[1]
    	pred = int(self.arg[2])
    	if ar == 'regression' and len(self.arg) == 3:
    		data = pd.read_csv(file)
    		print("Head Data:")
    		print(data.head())
    		X=data['YearsExperience'].values.reshape(30,1)
    		y=data['Salary']
    		X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.30, random_state = 42)
    		model = LinearRegression()
    		trained_model = model.fit(X_train,y_train)
    		print("Prediction on Test data: {}".format(trained_model.predict(X_test)))

    		print("Prediction for value {} is {}".format(pred,trained_model.predict([[pred]])))
    	else:
    		print("Argument must be valid")

