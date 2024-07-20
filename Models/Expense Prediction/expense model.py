import os
os.chdir('/Users/mariya/pers/Development/Python/Models/Expense Prediction')

import pandas as pd
data_df = pd.read_csv('Income_Expense_Data.csv')

print("Shape of the given dataset is: {0} Rows and {1} columns".format(data_df.shape[0], data_df.shape[1]))

print(data_df.head(10))

# Check for Null Values
print("Null Values in the Given Dataset")
print(data_df.isna().sum())

# Treat null values with median of the repsective column/variable
data_df['Income'].fillna((data_df['Income'].median()), inplace=True)

# Check for missing values after treating the dataset
print("Check for null values after treating the dataset")
print(data_df.isnull().sum())

# Check for outliers
print("Outlier Percentiles for the Variable Age")
outlier_percentiles = pd.DataFrame(data_df['Age']).describe(percentiles=(1,0.99, 0.9, 0.75, 0.5, 0.3, 0.1, 0.01))
print(outlier_percentiles)

print("Box plot to display the Outlier")
import matplotlib.pyplot as plt
# plt.boxplot(data_df['Age'])
plt.show()

print("Outlier Detection & Treatment using IQR Method")
# Get median Age
age_col_df = pd.DataFrame(data_df['Age'])
age_median = age_col_df.median()

# Get IQR of Age Variable
Q3 = age_col_df.quantile(q=0.75)
Q1 = age_col_df.quantile(q=0.25)
IQR = Q3 - Q1

# Derive boundaries of Outliers
IQR_LL = int(Q1 - 1.5*IQR)
IQR_UL = int(Q3 + 1.5*IQR)

# Finding and treating outliers - both lower & upper ends
data_df.loc[data_df['Age']>IQR_LL, 'Age '] = int(age_col_df.quantile(q=0.99))
data_df.loc[data_df['Age']<IQR_UL, 'Age '] = int(age_col_df.quantile(q=0.01))

print("Now box plotting Age after outlier treatment")
# plt.boxplot(data_df['Age'])
plt.show()

data_df = data_df.iloc[:, :-1]

# EDA
print("******** EDA *********")
x = data_df['Income']
y = data_df['Expense']

# Scatter Plot
# plt.scatter(x, y, label='Income Expense')
# plt.title("Income Vs Expense")
plt.show()

# Correlation Matrix
import seaborn as sns
print("***** Correlation Matrix ******")
correlation_matrix = data_df.corr().round(2)
f, ax = plt.subplots(figsize=(8,4))
# sns.heatmap(data = correlation_matrix, annot=True, cmap='PiYG')
plt.show()

# Scaling the Data
print("****** Scaling the Data using MinMaxScaler *******")
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
scaled_data = scaler.fit_transform(data_df)
print(scaled_data)

# Converting data back to pandas Dataframe
scaled_data_df = pd.DataFrame(scaled_data)
scaled_data_df.columns = ['Age', 'Income', 'Expense']

# Separating Input/Independent and Output/Dependent/Targert Varibales
features = ['Income', 'Age']
response = ['Expense']
X = scaled_data_df[features]
y = scaled_data_df[response]

# Dividing the data into train & test data
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=3, random_state=0)


# Model Building, and fitting the model\
from sklearn.linear_model import LinearRegression
from sklearn import metrics

model = LinearRegression()
model.fit(X_train, y_train)

# Check the accuracy of the model
accuracy = model.score(X_test, y_test)
print('Accuracy ', round(accuracy*100, 2),'%')

# print("***** X_test *****")
# print(X_test)

# print("***** y_test *****")
# print(y_test)

predicted_output = model.predict(X_test)
# print("***** Predicted Output from the Model *****")
# print(predicted_output)

intercept = model.intercept_
print("***** Intercept is: *****")
print(intercept)

coef = model.coef_
print("***** Coefficient is: *****")
print(coef)

# Creating the model equation
# Expense = (coef[0]*scaled_data[features[0]] - coef[1]*scaled_data[features[1]]) + intercept[0]
Expense = (0.59 * 0.35 - 0.32 * 0.26) + 0.06
print("***** Expense is: *****", Expense)

# ------------ Model Development is done as above ------------------------

# ============ Preparing the Model for deployment ========================
import pickle
pickle.dump(model, open('model.pkl', 'wb'))

# Reloading the model object
model = pickle.load(open('model.pkl', 'rb'))
print(model.predict([[30000, 24]]))






