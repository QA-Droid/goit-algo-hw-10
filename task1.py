from pulp import LpMaximize, LpProblem, LpVariable, value

model = LpProblem(name="production-optimization", sense=LpMaximize)

x1 = LpVariable(name="Lemonade", lowBound=0, cat="Integer")
x2 = LpVariable(name="Fruit_Juice", lowBound=0, cat="Integer")

model += x1 + x2, "Total_Products"
model += (2 * x1 + 1 * x2 <= 100), "Water_Constraint"
model += (1 * x1 <= 50), "Sugar_Constraint"
model += (1 * x1 <= 30), "Lemon_Juice_Constraint"
model += (2 * x2 <= 40), "Fruit_Puree_Constraint"
model.solve()

lemonade_count = value(x1)
fruit_juice_count = value(x2)
total_products = value(model.objective)

print(f"Кількість Лимонаду: {lemonade_count}")
print(f"Кількість Фруктового соку: {fruit_juice_count}")
print(f"Загальна кількість продуктів: {total_products}")