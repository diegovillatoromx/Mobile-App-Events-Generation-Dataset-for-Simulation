import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
file_path = 'your_path_here/simulated_data.csv'
data = pd.read_csv(file_path)

# Conversion Rate
total_sessions = len(data)
total_purchases = len(data[data['ORDER_TYPE'] == 'PURCHASE'])
conversion_rate = (total_purchases / total_sessions) * 100

print(f"Conversion Rate: {conversion_rate:.2f}%")

# Distribution of Payment Methods
# Filter only the rows where a purchase was made
purchase_data = data[data['ORDER_TYPE'] == 'PURCHASE']
payment_method_counts = purchase_data['PAYMENT_METHOD'].value_counts()

# Visualization settings
sns.set(style="whitegrid")

# Plot for Payment Method Distribution
plt.figure(figsize=(10, 6))
sns.barplot(x=payment_method_counts.values, y=payment_method_counts.index, palette="magma")
plt.title('Payment Method Distribution among Purchases')
plt.xlabel('Number of Purchases')
plt.ylabel('Payment Method')
plt.show()
