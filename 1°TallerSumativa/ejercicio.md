
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

1. Leer valores de \( \theta \) y \( \Delta x \) (con \( \Delta x = \Delta x_1 = \Delta x_2 \))
2. Para \( x_1 \) desde 0 hasta 5 con paso \( \Delta x \):
   1. Para \( x_2 \) desde 0 hasta 5 con paso \( \Delta x \):
      1. Si \( x_1 + x_2 \leq 5 \), calcular  
         \[
         f(x_1, x_2) = 1.20x_1 + 1.16x_2 - \theta \cdot (2x_1^2 + x_2^2 + (x_1 + x_2)^2)
         \]  
         y guardar la tupla \( \langle (x_1, x_2), f(x_1, x_2) \rangle \) en una lista
3. Buscar en la lista la tupla con el mayor valor de \( f(x_1, x_2) \)
4. Reportar la solución óptima \( \langle (x_1^*, x_2^*), f(x_1^*, x_2^*) \rangle \)

Este enfoque evalúa todas las combinaciones posibles bajo las restricciones, asegurando la solución global mediante una búsqueda exhaustiva.



