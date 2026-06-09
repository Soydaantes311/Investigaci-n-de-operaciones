import pulp

model = pulp.LpProblem("Cloud_Optimization", pulp.LpMinimize)

x1 = pulp.LpVariable("Almacenamiento Estandar", lowBound=0, cat='Integer')
x2 = pulp.LpVariable("Almacenamiento Premium ", lowBound=0, cat='Integer')

model += 20 * x1 + 60 * x2, "Costo_Total"

model += x1 + 3 * x2 >= 15, "IOPS"

model += 2 * x1 + 2 * x2 >= 14, "Disponibilidad"

model.solve()

print(f"Estado: {pulp.LpStatus[model.status]}")
print(f"Almacenamiento Estándar: {x1.varValue}")
print(f"Almacenamiento Premium: {x2.varValue}")
print(f"Costo Total Mensual: ${pulp.value(model.objective)}")
