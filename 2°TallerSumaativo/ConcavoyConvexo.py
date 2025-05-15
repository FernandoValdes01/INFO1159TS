from sympy import symbols, sympify


def main(lam=0):
    x = symbols( 'x' )
    fun = input("ingrese su funcion: ")
    fun = sympify(fun)
    print("ingrese dos punto x1 y x2")
    x1 = float(input("x1: "))
    x2 = float(input("x2: "))
    while lam <= 1:
        a = fun.subs(x, lam*x1 + (1 - lam)*x2)
        b = lam * fun.subs(x, x1) + (1 - lam) * fun.subs(x, x2)
        if a < b:
            print("si")
        else:
            print("no")
        lam += 0.1
    return

main()