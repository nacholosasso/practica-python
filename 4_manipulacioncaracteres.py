#Asignacion
mensaje ="Hola"
mensaje+=" "
mensaje+="Ernesto"
print(mensaje)


#Concatenacion
print("Concatenacion)")
mensaje= "hola"
espacio= " "
nombre= "Nacho"
print("mensaje + espacio + nombre")

numero_uno = 1
numero_dos= 2
resultado = numero_uno + numero_dos
resultado = str(resultado)
print("La suma de 1 + 2 es" +  " " +resultado)

#Busqueda

mensaje= "Hola Nacho"
nacho = mensaje.find("Nacho")
print(nacho) #Te devuelve la posicion del primer caracter de la palabra que buscas, en este caso la N de Nacho

#Extraccion
extraer_mensaje = mensaje[0:4]
print(extraer_mensaje) #Te devuelve el mensaje desde la posicion 0 hasta la posicion 4, sin incluir la posicion 4, en este caso Hola

#Comparacion
mensaje == nacho #Te devuelve un booleano, en este caso False porque mensaje es "Hola Nacho" y nacho es un numero entero que representa la posicion de la palabra Nacho en el mensaje
listo = "Listo"
listo2 = "Listo"
listo== listo2 #Te devuelve un booleano, en este caso True porque ambos mensajes son iguales
