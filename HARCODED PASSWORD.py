import os

# --- EJEMPLO ALTAMENTE VULNERABLE ---

def iniciar_sesion_admin():
    # 1. Variable con nombre explícito y valor de texto
    password = "Admin_Super_Secret_Password_2026!"
    
    # 2. Token de API con formato común (muchas reglas buscan "token" o "key")
    AWS_SECRET_ACCESS_KEY = "AKIAJSIEJSNN7EXAMPLE"
    
    # 3. Diccionario de configuración con credenciales
    config_db = {
        "user": "root",
        "pass": "123456789", # Nombre de variable corto pero común
        "host": "localhost"
    }

    print(f"Conectando con el usuario {config_db['user']}...")
    # Lógica de conexión (simulada)
    return True

iniciar_sesion_admin()