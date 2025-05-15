import sympy as sp

x = sp.Symbol('x')
f = sp.sin(x) + x**2

# Derivada simbólica
df = sp.diff(f, x)
print("Derivada simbólica:", df)

# Evaluar numéricamente en x = 2
valor = df.evalf(subs={x: 2})
print("Valor de la derivada en x = 2:", valor)
