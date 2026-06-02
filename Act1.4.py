from scipy.optimize import linprog

# x1 = Servidor Blade Estándar (10,000 EPS)
# x2 = Servidor Rack Pro      (25,000 EPS)
c = [-10000, -25000]

# Restricciones
# 1500*x1 + 4000*x2 <= 30000  (Presupuesto USD)
#    1*x1 +    3*x2 <= 24     (Espacio en Rack - Bahías)
#    2*x1 +    5*x2 <= 45     (Energía kW)
A = [
    [1500, 4000],  # Presupuesto
    [1, 3],        # Bahías de Rack
    [2, 5]         # Energía
]

b = [30000, 24, 45]

# Límites
# x1: Al menos 0 (sin máximo definido) -> (0, None)
# x2: Al menos 2 (SLA de redundancia)  -> (2, None)
bounds = [
    (0, None),  # Límites para Blade Estándar
    (2, None)   # Límites para Rack Pro (Mínimo 2 por SLA)
]

# Especificamos que AMBAS variables deben ser números enteros (1 = Entero)
# [1, 1] significa que tanto x1 como x2 son variables enteras.
integrality = [1, 1]

res = linprog(c, A_ub=A, b_ub=b, bounds=bounds, integrality=integrality, method='highs')

if res.success:
    blades_optimos = round(res.x[0])
    racks_optimos = round(res.x[1])
    eps_maximo = round(-res.fun)
    
    presupuesto_usado = (blades_optimos * 1500) + (racks_optimos * 4000)
    rack_usado = (blades_optimos * 1) + (racks_optimos * 3)
    energia_usada = (blades_optimos * 2) + (racks_optimos * 5)

    print("¡Despliegue de Infraestructura Optimizado con Éxito!\n")
    print("Configuración óptima para el nodo Edge:")
    print(f"--------------------------------------------------")
    print(f"  Servidores Blade Estándar a instalar: {blades_optimos}")
    print(f"  Servidores Rack Pro a instalar:       {racks_optimos}")
    print(f"--------------------------------------------------")
    print(f" Capacidad Máxima del Nodo: {eps_maximo:,} EPS (Eventos por segundo)")
    print(f"--------------------------------------------------")
    print("\nReporte de uso de recursos:")
    print(f" Capital utilizado: ${presupuesto_usado:,} USD de $30,000 USD")
    print(f" Espacio en Rack:    {rack_usado} de 24 bahías ocupadas")
    print(f" Energía Eléctrica:  {energia_usada} kW de 45 kW máximos")
else:
    print("No se encontró una combinación de servidores que cumpla con los requisitos.")

