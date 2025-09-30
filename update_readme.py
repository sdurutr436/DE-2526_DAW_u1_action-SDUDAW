import subprocess
import datetime
import time
import os
os.chdir(os.path.dirname(os.path.abspath(__file__))) # Con esto aseguro que se ejecuta en el directorio del script

def run_tests():
    pasados = 0
    try:
        result = subprocess.run(["pytest", "-q"], capture_output=True, text=True)
        output = result.stdout
        for line in output.splitlines():
            if "passed" in line and "%" not in line:
                parts = line.split()
                if len(parts) > 0 and parts[1] == "passed":
                    pasados = int(parts[0])
        return "✅ Tests correctos", pasados
    except subprocess.CalledProcessError:
        return "❌ Tests fallidos", pasados

def update_markdowns(status: tuple, tiempo_total: float):
    
    estado = status[0] + "\n" # Estado de los tests
    tests_pasados = status[1]
    hora_ejecucion = datetime.datetime.now().strftime(" -> %Y-%m-%d %H:%M:%S\n") # Formato de fecha y hora
    tiempo_ejecucion = estado + f"{tiempo_total:.2f} segundos\n" # Tiempo con 2 decimales
    
    # ---------------------
    
    # BLOQUE PARA README.md
    
    with open("README.md", "r", encoding="utf-8") as freadme:
        lines_readme = freadme.readlines()
        
    # Actualiza README.md
    new_lines_readme = []
    for line in lines_readme:
        new_lines_readme.append(line)
        if line.strip() == "## Estado de los tests":
            new_lines_readme.append(estado)
            new_lines_readme.append(hora_ejecucion + "\n")
    

    with open("README.md", "w", encoding="utf-8") as freadme:
        freadme.writelines(new_lines_readme)
    
    # FIN BLOQUE README.md
    
    # -------------------
    
    # BLOQUE PARA report.md
    
    # Checkea si report.md existe, sino se crea con encabezado
    if not os.path.exists("report.md"):
        with open("report.md", "w", encoding="utf-8") as freport:
            freport.write("# Reporte de tests\n\n")
            
    with open("report.md", "r", encoding="utf-8") as freport:
        lines_report = freport.readlines()
        
    # Añade nueva entrada al final de report.md
    
    with open("report.md", "w", encoding="utf-8") as freport:
        freport.writelines(lines_report)
        freport.write(tiempo_ejecucion)
        
    # FIN BLOQUE README.md
    
    # -------------------
    
    # BLOQUE PARA test-report.md
    
    # Checkea si test-report.md exists, sino, se crea con encabezado
    if not os.path.exists("test-report.md"):
        with open("test-report.md", "w", encoding="utf-8") as ftestreport:
            ftestreport.write("# Test Report\n\n")

    with open("test-report.md", "r", encoding="utf-8") as ftestreport:
        lines_test_report = ftestreport.readlines()
    
    with open("test-report.md", "w", encoding="utf-8") as ftestreport:
        ftestreport.writelines(lines_test_report)
        ftestreport.write(hora_ejecucion)
        ftestreport.write(tiempo_ejecucion)
        ftestreport.write(f"Tests pasados: {tests_pasados}\n\n")
        
    # FIN BLOQUE test-report.md


if __name__ == "__main__":
    start = time.time()
    status = run_tests()
    end = time.time()
    tiempo_total = end - start
    update_markdowns(status, tiempo_total)
