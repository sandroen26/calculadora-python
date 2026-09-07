#print("hola mundo")
#texto = "luz"
#num = "12345"

#input("ingrese su nombre: ")
#print(texto)

#titulo
print("***__ calculadora tradicional __***")

#pedimos los datos al usuario
numero1 = int(input("ingrse primer numero "))
operacion = input("elija que operacion desea: (+ - * / %) ")
numero2 = int(input("ingrse segundo numero "))

#ejecutamos la operacion que selecciono el usuario
#suma
if operacion == "+":
    resultado = numero1 +  numero2
#resta    
elif operacion == "-":
    resultado = numero1 -  numero2
#multiplicacion    
elif operacion == "*":
    resultado = numero1 *  numero2
#division
elif operacion == "/":
    resultado = numero1 //  numero2
#resto
elif operacion == "%":
    resultado = numero1 %  numero2

#en caso de que el resultado sea negativo, con esto lo revertimos haciendolo positivo.
if resultado < 0:
    resultado = -resultado
else:
    resultado

#imprimimos el resultado.
print(resultado)
print(type(resultado))