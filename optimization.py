from pulp import LpMaximize, LpProblem, LpVariable, value

model = LpProblem(name="profit-optimization", sense=LpMaximize)

product_A = LpVariable(name="Product_A", lowBound=0)
product_B = LpVariable(name="Product_B", lowBound=0)

model += 40 * product_A + 30 * product_B, "Total_Profit"

model += (2 * product_A + 1 * product_B <= 100, "Machine_Time")
model += (1 * product_A + 1 * product_B <= 80, "Labor_Time")

model.solve()

print("=== Optimization Results ===")
print("Product A:", value(product_A))
print("Product B:", value(product_B))
print("Max Profit:", value(model.objective))
