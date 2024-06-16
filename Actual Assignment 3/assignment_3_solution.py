import pandas as pd
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

file_path = 'c:/users/usman.shahid/downloads/Retail.xlsx'  
dataframe = pd.read_excel(file_path)

dataframe.dropna(inplace=True)
print("Empty columns in dataframeset are: ", end='')
print(dataframe.isna().count())

dataframe['CustomerID'] = dataframe['CustomerID'].astype(str)

dataframe['Amount'] = dataframe['Quantity'] * dataframe['UnitPrice']
monetary = dataframe.groupby('CustomerID')['Amount'].sum().reset_index()
monetary.columns = ['CustomerID', 'Monetary']

frequency = dataframe.groupby('CustomerID')['InvoiceNo'].count().reset_index()
frequency.columns = ['CustomerID', 'Frequency']

dataframe['InvoiceDate'] = pd.to_datetime(dataframe['InvoiceDate'], format='%d-%m-%Y %H:%M')

max_date = dataframe['InvoiceDate'].max()
dataframe['Recency'] = (max_date - dataframe.groupby('CustomerID')['InvoiceDate'].transform('max')).dt.days
recency = dataframe[['CustomerID', 'Recency']].drop_duplicates()

rfm = monetary.merge(frequency, on='CustomerID').merge(recency, on='CustomerID')

scaler = StandardScaler()
rfm_scaled = scaler.fit_transform(rfm[['Monetary', 'Frequency', 'Recency']])

kmeans = KMeans(n_clusters=4, random_state=42)
rfm['Cluster'] = kmeans.fit_predict(rfm_scaled)

silhouette_avg = silhouette_score(rfm_scaled, rfm['Cluster'])
print(f'Silhouette Score: {silhouette_avg}')

cluster_summary = rfm.groupby('Cluster').agg({
    'Recency': 'mean',
    'Frequency': 'mean',
    'Monetary': 'mean',
    'CustomerID': 'count'
}).reset_index()

cluster_summary.columns = ['Cluster', 'Mean Recency', 'Mean Frequency', 'Mean Monetary', 'Customer Count']

print(cluster_summary)
