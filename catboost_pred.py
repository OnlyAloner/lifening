""" Module to predict time series for the health prediction model """

import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from statsmodels.tsa.statespace.sarimax import SARIMAX
from catboost import CatBoostRegressor

columns= ['pulse','systolic_pressure','diastolic_pressure','oxygen_level','glucose','temperature']

df = pd.read_csv('time_series.csv', parse_dates=['date'], index_col='date')

total_size = len(df)
train_size = int(total_size * 0.75)

train = df.iloc[:train_size]
test = df.iloc[train_size:]

y_train = train['is_anomaly']
y_test = test['is_anomaly']
exog_train = train[columns]
exog_test = test[columns]

model = CatBoostRegressor()
model.fit(exog_train, y_train)
predict = model.predict(exog_test)

# model = SARIMAX(y_train, exog=exog_train, order=(0, 1, 1), seasonal_order=(1, 1, 1, 12))
# results = model.fit()
# predict = results.forecast(steps=len(y_test), exog=exog_test)

mse = mean_squared_error(y_test, predict)
print(f'Mean Squared Error: {mse}')

plt.figure(figsize=(10, 6))

plt.plot(y_train.index, y_train, label='Train Actual')
plt.plot(y_test.index, y_test, label='Test Actual')
plt.plot(y_test.index, predict, color='red', label='Predictions')
plt.title('Actual vs. Predicted Values')
plt.xlabel('Date')
plt.ylabel('Target Variable')
plt.legend(fontsize=20)
plt.text(y_train.index[0], max(y_test), f'MSE: {round(mse, 5)}', fontsize=30, color='red')
plt.show()
