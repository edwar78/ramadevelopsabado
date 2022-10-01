#funcion tradicional para sumar dos numeros

def sumar(numero1, numero2):
    return numero1+numero2

#invocando la funcion total
resultado= sumar(5,10)
print(f"la suma es: {resultado}")

if resultado > 10:
    print("Ganaste")
else:
    print("Perdio")