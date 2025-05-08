
def entradas():
     theta = float(input("Ingresa el valor de θ (theta): "))    
     delta_x = float(input("Ingresa el valor de Δx (delta x): "))
     fuerzabruta(theta,delta_x)

def fuerzabruta(deltaX,theta):
     lista = []
     for x1 in range(0,5):
          for x2 in range(0,5):
               lista.add(funcionobjetivoevaluator(x1,x2,theta))
     return lista
     

def funcionobjetivoevaluator(x1, x2, theta):
    respuesta=1.20*x1 + 1.16*x2 - theta*(2*x1**2 + x2**2 + (x1 + x2)**2)
    if x1+x2<=5000:
         print("a")