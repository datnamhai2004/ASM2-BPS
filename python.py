import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import pandas as pd


df = pd.read_csv("Data.csv")
print(df.head())
print(df.info())
df.fillna(df.mean(), inplace=True)
df.to_csv("CleanedSaleData.csv", index=False)
df['sale_date'] = pd.to_datetime(df['sale_date'])

plt.figure(figsize=(12, 6))
plt.plot(df['sale_date'], df['total_amount'], marker='o', color='b')
plt.title('Biểu đồ doanh thu theo ngày')
plt.xlabel('Ngày')
plt.ylabel('Doanh thu')
plt.grid(True)
plt.show()

X = df[['quantity', 'discount', 'tax_amount']]
y = df['total_amount']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

print(f'R^2 Score: {model.score(X_test, y_test)}')

future_data = [[5, 10, 15]]  
future_sales = model.predict(future_data)
print(f'Dự đoán doanh số: {future_sales[0]}')
