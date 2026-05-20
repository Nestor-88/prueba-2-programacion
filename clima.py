import os
import sys
import requests

def obtener_clima():
    # 1. Validación de variable de entorno (Error Tipo 1)
    api_key = os.getenv('API_KEY_PROYECTO')
    if not api_key:
        print("ERROR CRÍTICO: La variable de entorno 'API_KEY_PROYECTO' no está configurada.")
        sys.exit(1)
        
    # Configuración de ciudad por defecto (Sur de Chile)
    ciudad = "Puerto Montt"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={ciudad},CL&appid={api_key}&units=metric&lang=es"
    
    try:
        # Realizar la consulta con un timeout de 10 segundos
        response = requests.get(url, timeout=10)
        
        # 2. Manejo de error HTTP status (Error Tipo 2: p.ej. 404 o 401 Clave Inválida)
        if response.status_code == 401:
            print("ERROR 401: API Key inválida o no autorizada.")
            sys.exit(1)
        elif response.status_code == 404:
            print(f"ERROR 404: No se encontró la información para la ciudad: {ciudad}.")
            sys.exit(1)
        
        response.raise_for_status()
        data = response.json()
        
        # Procesamiento de >= 3 campos de datos
        temp = data['main']['temp']
        humedad = data['main']['humidity']
        descripcion = data['weather'][0]['description']
        
        print("==================================================")
        print(f" ALERTA CLIMÁTICA PARA VIAJEROS EN EL SUR DE CHILE ")
        print("==================================================")
        print(f"Ciudad Monitoreada : {ciudad}")
        # Campo 1: Temperatura
        print(f"Temperatura Actual : {temp}°C")
        # Campo 2: Humedad
        print(f"Humedad Ambiental  : {humedad}%")
        # Campo 3: Condición      
        print(f"Estado del Tiempo  : {descripcion.capitalize()}")
        print("==================================================")
        print("Consejo: El clima en el sur cambia rápido. ¡Lleva ropa impermeable!")
        print("==================================================")
        
    # 3. Manejo de errores de conexión/red (Error Tipo 3)
    except requests.exceptions.ConnectionError:
        print("ERROR DE CONEXIÓN: No se pudo establecer comunicación con el servidor de la API.")
        sys.exit(1)
        
    # 4. Manejo de error por tiempo de espera agotado (Error Tipo 4)
    except requests.exceptions.Timeout:
        print("ERROR DE TIMEOUT: La solicitud a la API ha tardado demasiado tiempo.")
        sys.exit(1)
        
    except requests.exceptions.RequestException as e:
        print(f"ERROR INESPERADO: {e}")
        sys.exit(1)

if __name__ == "__main__":
    obtener_clima()


