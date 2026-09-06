#print("hola mundo")
#texto = "luz"
#num = "12345"

#input("ingrese su nombre: ")
#print(texto)

print("***__ calculadora tradicional __***")

numero1 = int(input("ingrse primer numero "))
operacion = input("elija que operacion desea: (+ - * / %) ")
numero2 = int(input("ingrse segundo numero "))

if operacion == "+":
    resultado = numero1 +  numero2
    
elif operacion == "-":
    resultado = numero1 -  numero2
    
elif operacion == "*":
    resultado = numero1 *  numero2

elif operacion == "/":
    resultado = numero1 //  numero2

elif operacion == "%":
    resultado = numero1 %  numero2


if resultado < 0:
    resultado = -resultado
else:
    resultado

print(resultado)