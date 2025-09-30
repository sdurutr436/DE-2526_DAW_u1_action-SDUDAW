import subprocess
import datetime
import time
import os
os.chdir(os.path.dirname(os.path.abspath(__file__))) # Con esto aseguro que se ejecuta en el directorio del script

def run_tests():
    try:
        subprocess.check_call(["pytest", "-q"])
        return "✅ Tests correctos"
    except subprocess.CalledProcessError:
        return "❌ Tests fallidos"

def update_markdowns(status: str, tiempo_total: float):
    
    estado = status + "\n"
    hora_ejecucion = datetime.datetime.now().strftime(" -> %Y-%m-%d %H:%M:%S\n")
    
    #Apertura de README.md y report.md
    with open("README.md", "r", encoding="utf-8") as freadme:
        lines_readme = freadme.readlines()
        
    new_lines_readme = []
    for line in lines_readme:
        new_lines_readme.append(line)
        if line.strip() == "## Estado de los tests":
            new_lines_readme.append(estado)
            new_lines_readme.append(hora_ejecucion + "\n")
    

    with open("README.md", "w", encoding="utf-8") as freadme:
        freadme.writelines(new_lines_readme)
    
    # Check if report.md exists, if not, create it with a header
    if not os.path.exists("report.md"):
        with open("report.md", "w", encoding="utf-8") as freport:
            freport.write("# Reporte de tests\n\n")
            
    with open("report.md", "r", encoding="utf-8") as freport:
        lines_report = freport.readlines()
    # Only add one entry per run, tiempo_total will be passed from main
    new_entry = estado + f"{tiempo_total:.2f} segundos\n"
    with open("report.md", "w", encoding="utf-8") as freport:
        freport.writelines(lines_report)
        freport.write(new_entry)

if __name__ == "__main__":
    start = time.time()
    status = run_tests()
    end = time.time()
    tiempo_total = end - start
    update_markdowns(status, tiempo_total)
