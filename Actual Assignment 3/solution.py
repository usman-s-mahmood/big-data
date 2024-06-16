import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

# Load the dataset
file_path = '/mnt/data/OnlineRetail.csv'  
data = pd.read_csv(file_path)

# Drop rows with missing values
data.dropna(inplace=True)

# Convert CustomerID to string
data['CustomerID'] = data['CustomerID'].astype(str)

# Compute the total amount spent by each customer
data['Amount'] = data['Quantity'] * data['UnitPrice']
monetary = data.groupby('CustomerID')['Amount'].sum().reset_index()
monetary.columns = ['CustomerID', 'Monetary']

# Compute the number of transactions (frequency) by each customer
frequency = data.groupby('CustomerID')['InvoiceNo'].count().reset_index()
frequency.columns = ['CustomerID', 'Frequency']

# Convert InvoiceDate to datetime
data['InvoiceDate'] = pd.to_datetime(data['InvoiceDate'], format='%d-%m-%Y %H:%M')

# Compute the recency (days since last purchase)
max
max_date = data['InvoiceDate'].max()
data['Recency'] = (max_date - data.groupby('CustomerID')['InvoiceDate'].transform('max')).dt.days
recency = data[['CustomerID', 'Recency']].drop_duplicates()

# Merge the monetary, frequency, and recency dataframes
rfm = monetary.merge(frequency, on='CustomerID').merge(recency, on='CustomerID')

# Standardize the data
scaler = StandardScaler()
rfm_scaled = scaler.fit_transform(rfm[['Monetary', 'Frequency', 'Recency']])

# Apply K-means clustering
kmeans = KMeans(n_clusters=4, random_state=42)
rfm['Cluster'] = kmeans.fit_predict(rfm_scaled)

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
# -- full script for this solution is below
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

# Load the dataset
file_path = '/mnt/data/OnlineRetail.csv'  # replace this with the actual file path
data = pd.read_csv(file_path)

# Drop rows with missing values
data.dropna(inplace=True)

# Convert CustomerID to string
data['CustomerID'] = data['CustomerID'].astype(str)

# Compute the total amount spent by each customer
data['Amount'] = data['Quantity'] * data['UnitPrice']
monetary = data.groupby('CustomerID')['Amount'].sum().reset_index()
monetary.columns = ['CustomerID', 'Monetary']

# Compute the number of transactions (frequency) by each customer
frequency = data.groupby('CustomerID')['InvoiceNo'].count().reset_index()
frequency.columns = ['CustomerID', 'Frequency']

# Convert InvoiceDate to datetime
data['InvoiceDate'] = pd.to_datetime(data['InvoiceDate'], format='%d-%m-%Y %H:%M')

# Compute the recency (days since last purchase)
max_date = data['InvoiceDate'].max()
data['Recency'] = (max_date - data.groupby('CustomerID')['InvoiceDate'].transform('max')).dt.days
recency = data[['CustomerID', 'Recency']].drop_duplicates()

# Merge the monetary, frequency, and recency dataframes
rfm = monetary.merge(frequency, on='CustomerID').merge(recency, on='CustomerID')

# Standardize the data
scaler = StandardScaler()
rfm_scaled = scaler.fit_transform(rfm[['Monetary', 'Frequency', 'Recency']])

# Apply K-means clustering
kmeans = KMeans(n_clusters=4, random_state=42)
rfm['Cluster'] = kmeans.fit_predict(rfm_scaled)

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
