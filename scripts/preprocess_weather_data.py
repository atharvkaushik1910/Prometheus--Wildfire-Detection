import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# Loading sample data
df = pd.read_csv('data/sample_weather.csv')

# Normalization using Min-Max Scaling
scaler = MinMaxScaler()
normalized = scaler.fit_transform(df.select_dtypes(include=['float64', 'int64']))

# Output
print("Normalized Data (first 5 rows):")
print(pd.DataFrame(normalized, columns=df.columns[1:]).head())

