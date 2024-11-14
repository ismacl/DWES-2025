from operaciones import suma, resta, multiplicacion, division

def calculadora():
    while True:
        try:
            #Solicita los dos numeros
            num1 = int(input("Introduce el primer numero:"))
            num2 = int(input("Introduce el segundo numero:"))

            #Solicita el tipo de operacion

            operacion = input("Elige la operacion (+, -, *, /): ")

            #Realiza la operacion segun la eleccion

            if operacion == '+':
                resultado = suma(num1, num2)
            elif operacion == '-':
                resultado = resta(num1, num2)
            elif operacion == '*':
                resultado = multiplicacion(num1, num2)
            elif operacion == '/':
                resultado = division(num1, num2)
            else:
                print ("Operacion no valida")
            
            #Muestra el resultado
            print ("El resultado es:", resultado)

            #Pregunta si desea hacer otra operacion

            continuar = input("Quieres hacer otra operacion? (s/n): ")
            if continuar == 'n':
                print("Saliendo de la calculadora")
                break
        except ValueError:
            print("Error introduce formato valido")

# Llama a la función calculadora
if __name__ == "__main__":
    calculadora()

