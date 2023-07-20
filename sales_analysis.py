import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
rajssdata = pd.read_csv("/Users/rajshekharsingh/Downloads/apple_products.csv")

highest_rated=rajssdata.sort_values(by=["Star Rating"], ascending=False)
highest_rated= highest_rated.head(10)
print(highest_rated['Product Name'])
print(rajssdata.head())
print(rajssdata.isnull().sum())
print(rajssdata.describe())
figure=px.scatter(data_frame=rajssdata, x="Number Of Ratings", y="Discount Percentage", size="Sale Price", trendline="ols", title="Relationship between Discount Percentage and number of ratings of iphones")
figure.show()

