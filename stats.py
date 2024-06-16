import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

cred = credentials.Certificate('serviceAccountKey.json')
firebase_admin.initialize_app(cred)

db = firestore.client()

collection_ref = db.collection('lifts')
docs = collection_ref.stream()
data = [doc.to_dict() for doc in docs]

df = pd.DataFrame(data)

print(df.head(30), '\n')
print(df.info(), '\n')
print(df.describe(include='all'), '\n')
print(df.isnull().sum(), '\n')

df['workHeight'] = df['workHeight'].astype(float)
df['liftStrenght'] = df['liftStrenght'].astype(float)

# print(df['liftAccesibility'].value_counts(), '\n')
# df.dropna(col=['liftAccesibility'], inplace=True)


























# plt.figure(figsize=(10, 6))
# sns.histplot(data=df, x='workHeight', kde=True)
# plt.title('Distribution of Work Heights')
# plt.show()