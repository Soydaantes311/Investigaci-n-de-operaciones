from scipy.optimize import linprog

# Función Objetivo: Maximizar Z = 2*x1 + 5*x2 -> Minimizar -2*x1 - 5*x2
# x1 = GB con Inspección Básica
# x2 = GB con Inspección Profunda
c = [-2, -5]

# Restricciones
# 1*x1 + 3*x2 <= 18  (Restricción de CPU)
# 1*x1 + 1*x2 <= 8   (Restricción de RAM)
A = [
    [1, 3],  # Coeficientes de CPU
    [1, 1]   # Coeficientes de RAM
]

b = [18, 8]

x1_bounds = (0, None)
x2_bounds = (0, None)


res = linprog(c, A_ub=A, b_ub=b, bounds=[x1_bounds, x2_bounds], method='highs')

if res.success:
    print("¡Optimización exitosa!\n")
    print(f"Resultados óptimos por segundo:")
    print(f"---------------------------------")
    print(f"Tráfico en Inspección Básica (x1): {res.x[0]:.2f} GB")
    print(f"Tráfico en Inspección Profunda (x2): {res.x[1]:.2f} GB")
    print(f"---------------------------------")
    # Multiplicamos por -1 para recuperar el valor máximo real de la seguridad
    print(f"Puntos de mitigación máximos (Seguridad total): {-res.fun:.2f} puntos")
else:
    print("No se pudo encontrar una solución óptima.")
