## Desafíos y soluciones del proyecto

Durante el desarrollo del sistema de gestión de biblioteca, se enfrentaron varios desafíos que fueron resueltos con distintas estrategias:

1. **Organización modular del código**  
   - **Desafío:** Inicialmente no estaba claro qué funciones debían ir en `main.py`, `funciones.py`, `validaciones.py` o `gestion_datos.py`.  
   - **Solución:** Se definieron criterios claros:
     - `main.py`: flujo principal y menú interactivo.  
     - `funciones.py`: funciones auxiliares de procesamiento de datos (normalización, generación de IDs, etc.).  
     - `validaciones.py`: funciones que validan datos o credenciales.  
     - `gestion_datos.py`: funciones que operan sobre las estructuras de datos del sistema (libros, préstamos, usuarios).  

2. **Documentación técnica**  
   - **Desafío:** Determinar cómo documentar el sistema: directamente en el código, en un archivo aparte o ambos.  
   - **Solución:** Se implementaron docstrings detallados en cada módulo y función, explicando propósito, parámetros, retornos y dependencias. Esto permite tener la documentación dentro del código y mantener un documento aparte para entrega formal.  

3. **Gestión de préstamos y usuarios**  
   - **Desafío:** Registrar préstamos de libros y relacionarlos con usuarios, incluyendo control de estado (`Disponible` / `Prestado`) y validación de existencia del usuario.  
   - **Solución:**  
     - Se creó la lista `prestamos` con `id`, `titulo` y `usuario`.  
     - Las funciones `registrar_prestamo` y `eliminar_prestamo` actualizan tanto el estado del libro como la lista de préstamos.  
     - Se implementaron validaciones para impedir prestar un libro a un usuario inexistente o prestar un libro ya prestado.  

4. **Implementación de recursividad en el login**  
   - **Desafío:** Se requería usar recursividad para el login, lo cual no es la práctica más común en sistemas reales.  
   - **Solución:** Se implementó `login(intentos=3)` de manera recursiva, contando intentos y bloqueando el acceso tras 3 intentos fallidos mediante `sys.exit()`.  

5. **Manejo de datos y normalización**  
   - **Desafío:** Comparar entradas del usuario con libros y nombres podía fallar por mayúsculas, tildes o caracteres especiales.  
   - **Solución:** Se creó la función `normalizar_titulo` que estandariza cadenas eliminando tildes y convirtiendo todo a minúsculas, asegurando búsquedas confiables.  

6. **Validaciones no usadas directamente**  
   - **Desafío:** Algunas funciones de validación, como `verificar_correo`, estaban implementadas pero no se integraban al flujo principal.  
   - **Solución:** Se documentaron y se mantienen listas para futuras expansiones del sistema, dejando claro en la documentación que actualmente no se utilizan.  
