#--------------------------------------------------------------------------------------------------
# Funcion principal
def entradas():
    # se ingresa theta que define el valor del riesgo 
    theta = float(input("Ingresa el valor de θ (theta): "))
    # delta define la resolucíon con la que se recorre el dominio de x1 y x2    
    delta_x = float(input("Ingresa el valor de Δx (delta x): "))

    # se retorna la lista con tuplas de 3 con valores suboptimos que cumplan con la restrición 
    # (x1 , x2 , valor de la funcion)
    resultados = fuerzabruta(theta, delta_x)
    
    # Busca el mayor valor de la lista "resultados" pero solo comparando el tercer valor (x[2])
    # y lo imprime
    mejor = max(resultados, key=lambda x: x[2])
    print(f"x1 = {mejor[0]}, x2 = {mejor[1]}, valor = {mejor[2]}")
#--------------------------------------------------------------------------------------------------
# Funcion de fuerza bruta
# busca los valores suboptimos que cumplan la condicion 
def fuerzabruta(theta, deltaX, A=5000):
    lista = []
    x1 = 0.0
    while x1 <= A:
        x2 = 0.0
        while x2 <= A:
            if x2 + x1 <= A:
                # se evalua los valores de x1 y x2 con theta en la funcion 
                # para que retorne un valor suboptimo
                valor = objetivo(x1, x2, theta)
                # guarda en una lista la tupla de x1-x2 y el valor suboptimo en ese punto
                lista.append((x1, x2, valor))
            x2 += deltaX
        x1 += deltaX
    return lista
#--------------------------------------------------------------------------------------------------
# Funcion que evalua los valores ingresados en la funcion matematica
def objetivo(x1, x2, theta):
    return 1.20*x1 + 1.16*x2 - (theta * (2*x1**2 + x2**2 + (x1 + x2)**2))
#--------------------------------------------------------------------------------------------------

#Main(){
entradas()
#return 0 
#}