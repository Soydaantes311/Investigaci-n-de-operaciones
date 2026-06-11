import pulp

model = pulp.LpProblem("VideoGame_Assets", pulp.LpMaximize)

x1 = pulp.LpVariable("Ilustracion", lowBound=0, cat='Integer')
x2 = pulp.LpVariable("Icono", lowBound=0, cat='Integer')

model += 40 * x1 + 20 * x2, "Valor_Total"

model += 2 * x1 + x2 <= 12, "Diseñador"

model += x1 + 8 * x2 <= 9, "H/Semanas"

model.solve()

print(f"Estado: {pulp.LpStatus[model.status]}")
print(f"Ilustracion: {x1.varValue}")
print(f"Icono: {x2.varValue}")
print(f"Valor Total: ${pulp.value(model.objective)}")
