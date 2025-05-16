
import matplotlib.pyplot as plt
from sympy import symbols, sympify, lambdify
import numpy as np


#------------------------------------------------------------------------------
def main():
    x = symbols( 'x' )
    fun = input("ingrese su funcion: ")
    fun = sympify(fun)
    print("ingrese dos punto x1 y x2")
    x1 = float(input("x1: "))
    x2 = float(input("x2: "))
    convex, concav = veri(x1,x2,x,fun)
    if convex and not concav:
        print("convexa en todo el intervalo.")
    elif concav and not convex:
        print("cóncava en todo el intervalo.")
    elif convex and concav:
        print("lineal.")
    else:
        print("ni convexa ni cóncava.")

    graficar(x, fun, x1, x2)
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
def veri(x1,x2,x,fun,lam=0.0):
    epsilon = 1e-6
    Cx, Cv = True, True
    while lam <= 1:
        a = fun.subs(x, lam*x1 + (1 - lam)*x2)
        b = lam * fun.subs(x, x1) + (1 - lam) * fun.subs(x, x2)
        if abs(a - b) < epsilon:
            lam += 0.1
            continue
        elif a < b:
            Cv = False
        elif a > b:
            Cx = False
        lam += 0.1
    return Cx,Cv
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
def graficar(x, fun, x1, x2):
    f_lamb = lambdify(x, fun, modules=['numpy'])
    
    xs = np.linspace(x1 - 1, x2 + 1, 300)
    ys = f_lamb(xs)

    # Cuerda entre f(x1) y f(x2)
    cuerda_x = [x1, x2]
    cuerda_y = [f_lamb(x1), f_lamb(x2)]

    plt.plot(xs, ys, label='f(x)', linewidth=2)
    plt.plot(cuerda_x, cuerda_y, 'r--', label='Cuerda f(x1) a f(x2)', linewidth=2)
    plt.scatter([x1, x2], [f_lamb(x1), f_lamb(x2)], color='black')
    plt.title('Visualización de la función y su cuerda')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.legend()
    plt.grid(True)
    plt.show()
#------------------------------------------------------------------------------


main()