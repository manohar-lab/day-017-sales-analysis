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
import matplotlib.pyplot as plt

# 🔹 BAR CHART (Category-wise Sales)
plt.figure()
category_sales.plot(kind="bar")
plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Amount")
plt.show()


# 🔹 PIE CHART (Distribution)
plt.figure()
category_sales.plot(kind="pie", autopct="%1.1f%%")
plt.title("Sales Distribution")
plt.ylabel("")
plt.show()
top_products = df.sort_values(by="amount", ascending=False).head(3)

print("\nTop 3 Products:")
print(top_products)