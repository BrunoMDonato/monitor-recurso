import psutil
import time

def obtener_uso_recursos():
    uso_cpu = psutil.cpu_percent(interval=1)
    uso_memoria = psutil.virtual_memory().percent
    return uso_cpu, uso_memoria

if __name__ == "__main__":
    print("🔍 Monitoreo de Recursos del Sistema")
    try:
        while True:
            cpu, memoria = obtener_uso_recursos()
            print(f"💻 CPU: {cpu}% | 🟢 RAM: {memoria}%")
            time.sleep(2)  # Actualiza cada 2 segundos
    except KeyboardInterrupt:
        print("\n🛑 Monitoreo detenido.")
