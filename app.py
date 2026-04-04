import pandas as pd
df = pd.read_csv("sales.csv")

print("\nAll Data:")
total = df["amount"].sum()
print("\nTotal Sales:", total)
category_sales = df.groupby("category")["amount"].sum()
print("\nSales by Category:")
print(category_sales.reset_index())
top_category = category_sales.idxmax()
print("\nTop Category:", top_category)
top_product = df.loc[df["amount"].idxmax()]
print("\nTop Product:")
print(top_product.to_string())
print("\nAverage Sales :", df["amount"].mean())