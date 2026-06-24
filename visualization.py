import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("automobile.csv.csv")

print(df.head())

# -------------------------
# Visualization 1
# Average Price by Car Body
# -------------------------

plt.figure(figsize=(8,5))

df.groupby("carbody")["price"].mean().sort_values().plot(
    kind="bar"
)

plt.title("Average Price by Car Body Type")
plt.ylabel("Average Price")

plt.tight_layout()

plt.savefig("price_by_carbody.png")

plt.show()

# -------------------------
# Visualization 2
# Horsepower vs Price
# -------------------------

plt.figure(figsize=(8,5))

sns.scatterplot(
    data=df,
    x="horsepower",
    y="price"
)

plt.title("Horsepower vs Price")

plt.tight_layout()

plt.savefig("horsepower_vs_price.png")

plt.show()

# -------------------------
# Visualization 3
# Correlation Heatmap
# -------------------------

numeric_df = df.select_dtypes(include=["number"])

plt.figure(figsize=(12,8))

sns.heatmap(
    numeric_df.corr(),
    annot=True,
    cmap="coolwarm"
)

plt.title("Correlation Heatmap")

plt.tight_layout()

plt.savefig("correlation_heatmap.png")

plt.show()

# -------------------------
# Visualization 4
# Fuel Economy Analysis
# -------------------------

plt.figure(figsize=(8,5))

sns.scatterplot(
    data=df,
    x="citympg",
    y="price"
)

plt.title("City MPG vs Price")

plt.tight_layout()

plt.savefig("fuel_economy_analysis.png")

plt.show()

print("\nVisualization Project Completed Successfully!")
