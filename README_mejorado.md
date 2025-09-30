# Automatización de tests y actualización de documentación


## Puntos cumplidos
- Historial de resultados: Se guardan en README.md a medida que se ejecutan, indicando si pasan o no.
- Generar archivo ```report.md´´´ el cual se actualiza con la información más detallada.

## Puntos extra cumplidos
- Guardado histórico de las pruebas en README.md, no se sobreescribe la información, va añadiendola.
- Añadida la captura de los tests pasados, haciendo un contador de cantidad de tests que se pasan.


---

## Cambios principales y motivos

### 1. Establecer el directorio de trabajo
```python
os.chdir(os.path.dirname(os.path.abspath(__file__)))
```
- **Original:** El script asumía que siempre se ejecutaba en el mismo directorio.  
- **Cambio:** Ahora fuerzo a que el script se ejecute en la ruta donde está guardado. 
- **Motivo:** Evito errores de rutas relativas que estaban pasandome originalmente en una de las pruebas. El script no detectaba donde se encontraba.

---

### 2. Medición del tiempo de ejecución
```python
start = time.time()
...
end = time.time()
tiempo_total = end - start
```
- **Original:** Solo devolvía si los tests pasaban o fallaban.   
- **Cambio:** Ahora calculo cuánto tardan en correr todos los tests.   

---

### 3. Registro de la hora exacta de la ejecución
```python
hora_ejecucion = datetime.datetime.now().strftime(" -> %Y-%m-%d %H:%M:%S\n")
```
- **Original:** No se registraba cuándo se habían ejecutado los tests.  
- **Cambio:** Ahora guardo la fecha y hora de cada ejecución en el `README.md`.  
- **Motivo:** Me permite saber si los resultados están actualizados y tener trazabilidad.

---

### 4. Creación de un reporte histórico (`report.md`)
- **Original:** Solo actualizaba el `README.md`.  
- **Cambio:** Ahora también creo/actualizo un archivo `report.md` donde se va acumulando un histórico de ejecuciones (estado + duración).  
- **Motivo:** El `README.md` refleja el estado actual, pero el `report.md` me da un registro cronológico completo de todas las pruebas.

---

### 5. Mejoras en la escritura de archivos
- **Original:** Insertaba el estado y cortaba la escritura al primer `## Estado de los tests`.  
- **Cambio:** Además del estado, ahora incluyo la hora en `README.md` y en `report.md` agrego cada ejecución sin sobrescribir el historial.  
- **Motivo:** Más claridad y persistencia de la información.

---

## Conclusión

El código original era funcional y cumplía lo básico: mostrar si los tests habían pasado o fallado en el `README.md`.  

Con los cambios que hice ahora tengo:  
- Control total del directorio de ejecución.  
- Registro de la hora de cada prueba.  
- Medición del tiempo de ejecución.  
- Un historial acumulado en `report.md`.  

Esto convierte un simple script de verificación en una herramienta de monitoreo más completa y confiable para mis tests.
