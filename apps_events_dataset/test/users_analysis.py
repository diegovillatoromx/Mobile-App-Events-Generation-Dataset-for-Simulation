import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Loading the CSV file
file_path = 'your_path_here/simulated_data.csv'
data = pd.read_csv(file_path)

# Visualization settings
sns.set(style="whitegrid")

# Analysis of User Distribution by City
city_counts = data['CITY'].value_counts()

# Plot for User Distribution by City
plt.figure(figsize=(10, 6))
sns.barplot(x=city_counts.values, y=city_counts.index, palette="viridis")
plt.title('User Distribution by City')
plt.xlabel('Number of Users')
plt.ylabel('City')
plt.show()

# Analysis of Operating System Distribution
os_counts = data['OS_USER'].value_counts()

# Plot for Operating System Distribution
plt.figure(figsize=(10, 6))
sns.barplot(x=os_counts.values, y=os_counts.index, palette="magma")
plt.title('Operating System Distribution')
plt.xlabel('Number of Users')
plt.ylabel('Operating System')
plt.show()
