import pandas as pd
import matplotlib.pyplot as plt

# Read data from the cleaned CSV file
df = pd.read_csv("SaleData.csv")

# Bar Chart: Total sales by month
df['sale_date'] = pd.to_datetime(df['sale_date'])  # Convert 'sale_date' column to datetime format
df['month'] = df['sale_date'].dt.month  # Extract month from 'sale_date' column
monthly_sales = df.groupby('month')['total_amount'].sum()

plt.figure(figsize=(10, 6))
plt.bar(monthly_sales.index, monthly_sales.values)
plt.xlabel('Month')
plt.ylabel('Total Sales')
plt.title('Total Sales by Month')
plt.xticks(monthly_sales.index)
plt.show()

# Line Chart: Daily sales fluctuations
daily_sales = df.groupby('sale_date')['total_amount'].sum()

plt.figure(figsize=(12, 6))
plt.plot(daily_sales.index, daily_sales.values, marker='o', linestyle='-')
plt.xlabel('Day')
plt.ylabel('Total Sales')
plt.title('Daily Sales Fluctuations')
plt.xticks(rotation=45)
plt.show()

# Box Plot: Sales distribution
plt.figure(figsize=(8, 6))
plt.boxplot(df['total_amount'])
plt.ylabel('Sales')
plt.title('Sales Distribution')
plt.show()
