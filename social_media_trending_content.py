# -*- coding: utf-8 -*-

import pandas as pd
from typing import Mapping

df = pd.read_csv('Cleaned_Viral_Social_Media_Trends.csv')
df.head()

Mapping={"Low":0,"Medium":1,"High":2}
df['numeric_level'] =df['Engagement_Level'].map(Mapping)

df['is_trending']=df['Engagement_Level'].apply(lambda x:"low"if x =='Low' else ("Medium" if x== "Medium" else "High" ))
df['is_trending'].value_counts()

df['is_trending']=df['is_trending'].str.lower()
trending_df = df[df['is_trending'].isin(["medium","high"])]
print(trending_df["Hashtag"])

print(trending_df[["Hashtag","Engagement_Level","is_trending"]])