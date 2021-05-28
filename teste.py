import pandas as pd
from pandas.io.json import json_normalize
import numpy
import requests as re
import json
import os
from IPython.display import JSON
import sqlite3
from sqlite3 import Error
res = re.get('https://api.yelp.com/v3/businesses/search?latitude=43.7777875391617&longitude=-79.26400584572922', headers={'Authorization': 'Bearer 5zcKBU6D7WI4xTPA4kR6bmG-Bpdyrp9Ncrau45Qk8lpWU2mzEkKbQDfKYtePTMhFyIVm8c90Phvd2h4vBV8Nu6Og2Xeh6FNoH-AzaVN1EOTQd8GPpbbg2Fj0P2BKYHYx'})
result = res.json()
df = pd.DataFrame(result['businesses'])
df2 = df[['name', 'rating', 'review_count', 'location', 'categories']].copy()
x = 0
for rewr in df2:
    df2.iloc[x,4] = df2.iloc[x,4][0]['alias']
    x += 1
print(df2)