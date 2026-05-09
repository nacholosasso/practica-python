palabra = input("Introduce una palabra: ") #te pide un dato desde el telcado, lo que escribas se guarda en la variable palabra
print("La palabra que has introducido es: " + palabra) #imprime la palabra
numero = int(input("Introduce un numero: ")) #te pide un numero, lo que escribas se guarda en la variable numero, pero como un string, por eso se usa int para convertirlo a entero
print("El numero que has introducido es: " + str(numero)) #imprime el
num_float = float(input("Introduce un numero decimal: ")) #te pide un numero decimal, lo que escribas se guarda en la variable num_float, pero como un string, por eso se usa float para convertirlo a decimal
print("El numero decimal que has introducido es: " + str(num_float)) #imprime el numero decimal
num_complejo = complex(input("Introduce un numero complejo (en formato a+bj): ")) #te pide un numero complejo, lo que escribas se guarda en la variable num_complejo
print("El numero complejo que has introducido es: " + str(num_complejo)) #imprime el numero complejo
print("Otra opcion es", numero) # al poner la , no hace falta poner numero en string

nombre = input("Introduce tu nombre: ") #te pide un nombre, lo que escribas se guarda en la variable nombre
print("Hola " + nombre + "vamos a hacer una suma")
numero_uno = int(input("Introduce un numero: "))
numero_dos = int(input("Introduce otro numero: "))
resultado = numero_uno + numero_dos
print("El resultado de la suma es: " + str(resultado))



