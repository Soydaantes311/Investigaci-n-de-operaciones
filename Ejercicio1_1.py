import pulp

# 1. Definir el problema (Minimización)
model = pulp.LpProblem("Cloud_Optimization", pulp.LpMinimize)

# 2. Definir Variables (Enteras, ya que no puedes rentar media instancia)
x1 = pulp.LpVariable("Instancia_A", lowBound=0, upBound=40, cat='Integer')
x2 = pulp.LpVariable("Instancia_B", lowBound=0, upBound=30, cat='Integer')

# 3. Función Objetivo
model += 10 * x1 + 30 * x2, "Costo_Total"

# 4. Restricciones
model += 2 * x1 + 4 * x2 >= 100, "CPU_Demand"
model += 1 * x1 + 5 * x2 >= 80, "RAM_Demand"

# 5. Resolver y mostrar
model.solve()

print(f"Estado: {pulp.LpStatus[model.status]}")
print(f"Contratar Tipo A: {x1.varValue}")
print(f"Contratar Tipo B: {x2.varValue}")
print(f"Costo Mínimo Diario: ${pulp.value(model.objective)}")

#source .venv/bin/activate