from sympy import symbols, sympify, diff, lambdify
import numpy as np
import math
def obtener_funcion():
    expr_str = input("Ingrese la función f(x): ")
    try:
        expr = sympify(expr_str)
        return expr
    except:
        print("Error: La función ingresada no es válida.")
        exit()

def obtener_valor_float(mensaje):
    try:
        return float(input(mensaje))
    except:
        print("Error: Debe ingresar un número válido.")
        exit()

def derivada_exacta(expr):
    return diff(expr, x)

def buscar_delta_x(f_num, df_exact_num, x0, epsilon):
    # Regla general: Δx ≈ sqrt(eps_maquina) * x
    eps_maquina = 2.22e-16
    delta_x = math.sqrt(eps_maquina) * abs(x0 if x0 != 0 else 1)  # evitamos multiplicar por 0

    while delta_x < 1.0:  # ahora lo aumentamos en vez de disminuir
        derivada_numerica = (f_num(x0 + delta_x) - f_num(x0)) / delta_x
        valor_exacto = df_exact_num(x0)
        error = abs(valor_exacto - derivada_numerica)

        if error < epsilon:
            return delta_x, derivada_numerica, valor_exacto, error

        delta_x *= 2  # buscamos el primer Δx que cumple aumentando (menos errores de redondeo)

    return None, None, None, None

# ======= PROGRAMA PRINCIPAL =======

x = symbols("x")

# Entrada del usuario
f_expr = obtener_funcion()
x0 = obtener_valor_float("Ingrese el punto x0 donde evaluar la derivada: ")
epsilon = obtener_valor_float("Ingrese el valor de error absoluto epsilon (ej. 1e-5): ")

# Derivada simbólica
df_expr = derivada_exacta(f_expr)

# Conversiones a funciones numéricas
f_num = lambdify(x, f_expr, modules=["numpy"])
df_num = lambdify(x, df_expr, modules=["numpy"])

# Búsqueda de Δx adecuado
delta_x, derivada_numerica, valor_exacto, error = buscar_delta_x(f_num, df_num, x0, epsilon)

# Resultados
if delta_x is not None:
    print("\n===== RESULTADOS =====")
    print(f"Función ingresada: f(x) = {f_expr}")
    print(f"Derivada simbólica: df/dx = {df_expr}")
    print(f"Evaluada en x0 = {x0}")
    print(f"Derivada exacta en x0: {valor_exacto}")
    print(f"Derivada numérica con Δx = {delta_x:.2e}: {derivada_numerica}")
    print(f"Error absoluto: {error:.2e}")
else:
    print("No se encontró un valor de Δx que cumpla con el error especificado.")
