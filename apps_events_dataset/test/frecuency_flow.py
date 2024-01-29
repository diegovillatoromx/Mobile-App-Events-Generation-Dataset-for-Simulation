import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
file_path = 'your_path_here/simulated_data.csv'
data = pd.read_csv(file_path)

# Create a new column with the sequence of events
data['EVENT_FLOW'] = data[['INITIAL_EVENT', 'EVENT_2', 'EVENT_3', 'EVENT_OUT']].agg(' -> '.join, axis=1)

# Count the most common sequences
event_flows = data['EVENT_FLOW'].value_counts().head(10)

# Visualization settings
sns.set(style="whitegrid")

# Plot for Most Common Navigation Flows
plt.figure(figsize=(12, 8))
sns.barplot(y=event_flows.index, x=event_flows.values, palette="viridis")
plt.title('Most Common Navigation Flows')
plt.xlabel('Frequency')
plt.ylabel('Event Flow')
plt.show()
