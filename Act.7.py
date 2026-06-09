import pulp

model = pulp.LpProblem("VideoGame_Assets", pulp.LpMaximize)

x1 = pulp.LpVariable("Modelos_3D_Personajes", lowBound=0, cat='Integer')
x2 = pulp.LpVariable("Modelos_3D_Escenarios", lowBound=0, cat='Integer')

model += 80 * x1 + 60 * x2, "Valor_Total"

model += 2 * x1 + x2 <= 12, "GPU"

model += x1 + 2 * x2 <= 14, "VRAM"

model.solve()

print(f"Estado: {pulp.LpStatus[model.status]}")
print(f"Modelos 3D de Personajes: {x1.varValue}")
print(f"Modelos 3D de Escenarios: {x2.varValue}")
print(f"Valor Total: ${pulp.value(model.objective)}")
