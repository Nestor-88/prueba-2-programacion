# Monitoreo Climático Automatizado - Viajeros Sur de Chile

## 1. Contexto y Narrativa
* [cite_start]**Stakeholder (¿Quién usa la herramienta?):** Turistas independientes, mochileros y guías de trekking que recorren las regiones del sur de Chile (como la Patagonia, Puerto Montt o Torres del Paine)[cite: 13]. [cite_start]No es un usuario genérico; es un viajero en ruta que depende críticamente de las condiciones meteorológicas para su seguridad[cite: 14].
* **Propuesta de Valor (Problema/Solución):** El clima en el sur de Chile es extremadamente cambiante e impredecible (puede haber lluvia torrencial, viento fuerte y sol en un mismo día). [cite_start]Esta herramienta elimina la dificultad de quedar atrapado en senderos o rutas peligrosas sin el equipamiento adecuado[cite: 15]. [cite_start]Al realizar una consulta rápida y puntual desde la consola, el viajero obtiene el estado del tiempo en tiempo real para tomar decisiones de vestimenta o itinerario de forma inmediata[cite: 8, 15].

## 2. Guía de Configuración
[cite_start]Para que la aplicación funcione correctamente y se resguarde la seguridad técnica, está prohibido dejar las claves en el código[cite: 26]. [cite_start]Se debe configurar la siguiente variable de entorno en el sistema operativo[cite: 22]:

* [cite_start]`API_KEY_PROYECTO`: Token o llave de autenticación personal provista por la API de OpenWeatherMap[cite: 22, 55].

### Cómo configurar la variable de entorno localmente:
* [cite_start]En **Linux/Bash (DEVASC VM):** `export API_KEY_PROYECTO="tu_clave_secreta"` [cite: 56]
* [cite_start]En **Windows (PowerShell):** `$env:API_KEY_PROYECTO="tu_clave_secreta"` [cite: 56]

## 3. Instrucciones de Ejecución (Docker)
[cite_start]Esta aplicación realiza una consulta puntual y termina con un código de salida limpio (Exited 0), por lo que no requiere mantenerse en ejecución continua[cite: 9, 33].

### Opción A: Construcción y Ejecución Manual
[cite_start]Si desea correr el contenedor de forma manual paso a paso, use los siguientes comandos de Docker[cite: 23]:

1. **Construir la imagen desde el Dockerfile:**
   ```bash
   docker build -t clima-sur-app .
