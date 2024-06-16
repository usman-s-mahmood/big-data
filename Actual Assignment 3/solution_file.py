'''
**Programming with Big Data Assignment 3** 

**Section: D-3** 

**Group Members**

Usman Shahid (L1F22BSCS1057)
Anas Yousaf (L1F22BSCS1070)
Ahmad Sohail (L1F22BSCS1048)

Submitted to: Ms. Misbah Naz
'''
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt

# Loading The Dataset

data = pd.read_csv('Retail.csv')
data.head()

# Drop Rows with missing values

data.dropna(inplace=True)
print(data.isna().sum())

# converting customerID to String
data['CustomerID'] = data['CustomerID'].astype(str)
data.head()

# Compute the total amount spent by each customer

data['Amount'] = data['Quantity'] * data['UnitPrice']
monetary = data.groupby('CustomerID')['Amount'].sum().reset_index()
monetary.columns = ['CustomerID', 'Monetary']
print(monetary)

# Compute the number of transactions (frequency) by each customer

frequency = data.groupby('CustomerID')['InvoiceNo'].count().reset_index()
frequency.columns = ['CustomerID', 'Frequency']
print(frequency)

# Convert InvoiceDate to datetime

data['InvoiceDate'] = pd.to_datetime(data['InvoiceDate'], format='%d-%m-%Y %H:%M')

# Compute the recency (days since last purchase)

max_date = data['InvoiceDate'].max()
data['Recency'] = (max_date - data.groupby('CustomerID')['InvoiceDate'].transform('max')).dt.days
recency = data[['CustomerID', 'Recency']].drop_duplicates()
print(recency)

# Merge the monetary, frequency, and recency dataframes

rfm = monetary.merge(frequency, on='CustomerID').merge(recency, on='CustomerID')
print(rfm)

# Standardize the data
scaler = StandardScaler()
rfm_scaled = scaler.fit_transform(rfm[['Monetary', 'Frequency', 'Recency']])
print(rfm_scaled)

# Apply K-means clustering
kmeans = KMeans(n_clusters=4, random_state=42)
rfm['Cluster'] = kmeans.fit_predict(rfm_scaled)
print(f'{kmeans}')

# Compute the silhouette score
silhouette_avg = silhouette_score(rfm_scaled, rfm['Cluster'])
print(f'Silhouette Score: {silhouette_avg}')

# Analyze the clusters
cluster_summary = rfm.groupby('Cluster').agg({
    'Recency': 'mean',
    'Frequency': 'mean',
    'Monetary': 'mean',
    'CustomerID': 'count'
}).reset_index()

# Rename the columns for clarity
cluster_summary.columns = ['Cluster', 'Mean Recency', 'Mean Frequency', 'Mean Monetary', 'Customer Count']

# Display the cluster summary
print(cluster_summary)

# **Visualization of Clusters**
plt.figure(figsize=(8, 6))

colors = ['blue', 'green', 'red', 'purple']

for cluster_label, color in zip(range(4), colors):
    cluster_data = rfm[rfm['Cluster'] == cluster_label]
    plt.scatter(cluster_data['Frequency'], cluster_data['Monetary'], color=color, label=f'Cluster {cluster_label}')

plt.title('Visualizing Clusters of Customers')
plt.xlabel('Frequency')
plt.ylabel('Monetary')
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.show()
