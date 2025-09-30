import subprocess
import datetime
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

def run_tests():
    try:
        subprocess.check_call(["pytest", "-q"])
        return "✅ Tests correctos"
    except subprocess.CalledProcessError:
        return "❌ Tests fallidos"

def update_readme(status: str):
    
    hora_ejecucion = datetime.datetime.now().strftime("Última ejecución: %Y-%m-%d %H:%M:%S\n")
    
    with open("README.md", "r", encoding="utf-8") as f:
        lines = f.readlines()

    new_lines = []
    for line in lines:
        new_lines.append(line)
        if line.strip() == "## Estado de los tests":
            new_lines.append(status)
            new_lines.append(hora_ejecucion + "\n")

    with open("README.md", "w", encoding="utf-8") as f:
        f.writelines(new_lines)

if __name__ == "__main__":
    status = run_tests()
    update_readme(status)
