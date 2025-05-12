
# ACTIVIDAD 1
Por parejas o individualmente, deberán crear un video en YouTube en el que se explique el algoritmo programado para resolver modelos de programación no lineal mediante fuerza bruta. Coloquen el enlace al mismo en el editor que aparecerá, identificando a los miembros del grupo. En el caso de que el trabajo hubiese sido realizado grupalmente, solo uno de los miembros subirá la información, aunque ambos miembros deben participar en términos similares, tanto en tiempo como en importancia del contenido, en el vídeo. Si el enlace no funciona se tomará como una actividad "no entregada". Puede usar el lenguaje de programación de su preferencia. La rúbrica de evaluación se encuentra en documento adjunto. 


## Problema a resolver

Un inversor tiene US$5000 para invertir en dos potenciales instrumentos financieros, siendo x₁ y x₂ la cantidad invertida en cada uno de ellos. De datos históricos se espera que la inversión en el primero de ellos tenga una tasa de retorno de 20 %, mientras que la del segundo sea de 16 %. El riesgo, medido como la varianza del retorno total de la inversión, es dado por la función 2x₁² + x₂² + (x₁ + x₂)². Por tanto, el riesgo es una función tanto de la inversión en cada instrumento separado como de la inversión total. El inversor quisiera maximizar su retorno esperado a la vez que minimiza su riesgo.





## Modelamiento matemático

De manera general, no se podrían satisfacer ambos objetivos de manera simultánea. No obstante el retorno de la inversión y el riesgo pueden ser combinados en una función objetivo, obteniendo el siguiente modelo:

**Maximizar**  
f(x) = 1,20x₁ + 1,16x₂ − θ(2x₁² + x₂² + (x₁ + x₂)²)

**sujeto a:**

g₁(x) = x₁ + x₂ ≤ 5000  
x₁, x₂ ≥ 0  

donde θ refleja la compensación entre el riesgo y el retorno de la inversión, es decir, la aversión al riesgo del inversor.

## Resolución - Pseudocódigo

Para resolver el problema de inversión mediante fuerza bruta en el intervalo \( x_1, x_2 \in [0, 5] \), se propone el siguiente pseudocódigo:

1. Leer valores de θ y Δx (con Δx = Δx₁ = Δx₂)
2. Para x₁ desde 0 hasta 5 con paso Δx:
   1. Para x₂ desde 0 hasta 5 con paso Δx:
      1. Si x₁ + x₂ ≤ 5, calcular  
         f(x₁, x₂) = 1.20·x₁ + 1.16·x₂ − θ·(2·x₁² + x₂² + (x₁ + x₂)²)  
         y guardar la tupla ⟨(x₁, x₂), f(x₁, x₂)⟩ en una lista
3. Buscar en la lista la tupla con el mayor valor de f(x₁, x₂)
4. Reportar la solución óptima ⟨(x₁*, x₂*), f(x₁*, x₂*)⟩


Este enfoque evalúa todas las combinaciones posibles bajo las restricciones, asegurando la solución global mediante una búsqueda exhaustiva.



