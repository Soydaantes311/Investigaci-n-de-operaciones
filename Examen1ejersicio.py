import pulp

model = pulp.LpProblem("VideoGame_Assets", pulp.LpMaximize)

x1 = pulp.LpVariable("Servidores Basico", lowBound=0, cat='Integer')
x2 = pulp.LpVariable("Servidor avanzado", lowBound=0, cat='Integer')

model += 30 * x1 + 50 * x2, "Valor_Total"

model += 2 * x1 + x2 <= 24, "VGPU"

model += x1 + 2 * x2 <= 16, "RAM"

model.solve()

print(f"Estado: {pulp.LpStatus[model.status]}")
print(f"Servidor basico: {x1.varValue}")
print(f"Servidor avanzado: {x2.varValue}")
print(f"Valor Total: ${pulp.value(model.objective)}")
