import secrets
import string

def generar_password():
    # Definimos los grupos de caracteres
    letras = string.ascii_letters
    numeros = string.digits
    signos = "$!@#%^&*"
    
    # Combinamos todo para el resto de la password
    todos_los_caracteres = letras + numeros + signos
    
    # Aseguramos al menos un signo, un número y una letra
    password = [
        secrets.choice(signos),
        secrets.choice(numeros),
        secrets.choice(letras)
    ]
    
    # Completamos los 6 caracteres restantes para llegar a 9
    password += [secrets.choice(todos_los_caracteres) for _ in range(6)]
    #+= significa agregar lo que ya tenes a la variable
    
    # Mezclamos para que el signo no quede siempre al principio
    secrets.SystemRandom().shuffle(password)
    
    return "".join(password)

# Retornamos el resultado a la celda de Excel
retorno = generar_password()
retorno
