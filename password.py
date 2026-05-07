import secrets
import string

def generar_password():
    letras = string.ascii_letters
    numeros = string.digits
    signos = "$!@#%^&*"
    
    todos_los_caracteres = letras + numeros + signos
    
    password = [
        secrets.choice(signos),
        secrets.choice(numeros),
        secrets.choice(letras)
    ]
    
    password += [secrets.choice(todos_los_caracteres) for _ in range(6)]
    
    secrets.SystemRandom().shuffle(password)
    
    return "".join(password)

# --- CAMBIO AQUÍ ---
# En lugar de solo poner 'retorno', usamos print()
retorno = generar_password()
print(retorno)