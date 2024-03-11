from pulp import LpProblem, LpMaximize, LpVariable, lpSum

# Створення задачі
problem = LpProblem("Maximize_Products", LpMaximize)

# Оголошення змінних рішення
x1 = LpVariable("Lemonade", lowBound=0, cat="Integer")
x2 = LpVariable("Fruit_Juice", lowBound=0, cat="Integer")

# Функція максимізації
problem += x1 + x2, "Total_Products"

# Обмеження ресурсів
problem += 2 * x1 + x2 <= 100, "Water"
problem += x1 <= 50, "Sugar"
problem += x1 <= 30, "Lemon_Juice"
problem += 2 * x2 + x1 <= 40, "Fruit_Puree"

# Вирішення задачі
problem.solve()

# Виведення результатів
print("Maximized Total Products: {:.2f}".format(problem.objective.value()))
print("Lemonade: {:.2f} units".format(x1.value()))
print("Fruit Juice: {:.2f} units".format(x2.value()))