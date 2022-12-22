import math

weight = int(input('¿Cuál es tu peso en kg? '))
height = float(input('¿Cuál es tu estatura en m? '))

imc = weight /  height ** 2 

print(f"{imc:.2f}")