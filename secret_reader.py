import pandas as pd
import requests
import os

token=os.getenv("MY_SECRET_TOKEN")
print(f'Token:{token}')

response = requests.get("https://jsonplaceholder.typicode.com/users")
data=response.json()

df=pd.DataFrame(data)
print(df)