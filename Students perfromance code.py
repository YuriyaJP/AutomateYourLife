import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

# Load the dataset
data = pd.read_csv('performance.csv')

# Assuming 'project' is the column you want to use for clustering
project_data = data[['project']]

# Standardize the project scores
scaler = StandardScaler()
project_data_standardized = scaler.fit_transform(project_data)

# Perform K-Means clustering
kmeans = KMeans(n_clusters=3)  # You can change the number of clusters as needed
data['cluster'] = kmeans.fit_predict(project_data_standardized)

# Visualize the clusters
plt.scatter(data['student'], data['project'], c=data['cluster'], cmap='viridis')
plt.title('K-Means Clustering of Students Based on Project Scores')
plt.xlabel('Student ID')
plt.ylabel('Project Score')
plt.show()
