import codecademylib3
import pandas as pd

# 1. Load the data
inventory = pd.read_csv("inventory.csv")

# 2. Inspect the first 10 rows
print(inventory.head(10))

# 3. Staten Island location (first 10 rows)
staten_island = inventory.head(10)

# 4. Staten Island product descriptions
product_request = staten_island["product_description"]
print(product_request)

# 5. Brooklyn seed request
seed_request = inventory[(inventory.location == "Brooklyn") & (inventory.product_type == "seeds")]
print(seed_request)

# 6. Add in_stock column
inventory["in_stock"] = inventory["quantity"] > 0

# 7. Add total_value column
inventory["total_value"] = inventory["price"] * inventory["quantity"]

# 8. Combine product_type and product_description
combine_lambda = lambda row: "{} - {}".format(row.product_type, row.product_description)

# 9. Add full_description column
inventory["full_description"] = inventory.apply(combine_lambda, axis=1)

# Optional: show the updated inventory
print(inventory.tail())
