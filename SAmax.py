import threading
import time
import random

class Almacen:
    def __init__(self):
        self.stock = []  # Lista para almacenar las imágenes
        self.lock = threading.Lock()  # Mutex para controlar el acceso al almacén

    def agregar_imagen(self, imagen):
        with self.lock:
            self.stock.append(imagen)
            print(f"[+] Imagen agregada al almacén: {imagen}")

    def procesar_imagen(self):
        with self.lock:
            if self.stock:
                imagen = self.stock.pop(0)  # Extraer la primera imagen del almacén
                print(f"[-] MAX está procesando la imagen: {imagen}")
                return imagen
            else:
                print("[!] No hay imágenes en el almacén para procesar.")
                return None

class Max:
    def __init__(self, almacen):
        self.almacen = almacen
        self.lock = threading.Lock()  # Mutex para controlar el acceso de MAX

    def analizar_imagen(self):
        with self.lock:
            imagen = self.almacen.procesar_imagen()
            if imagen:
                time.sleep(1)  # Simula el tiempo lento de análisis
                print(f"[✓] MAX ha terminado de analizar la imagen: {imagen}")

def generar_imagenes(almacen):
    while True:
        num_imagenes = random.randint(0, 5)  # Generar entre 0 y 5 imágenes aleatoriamente
        for i in range(num_imagenes):
            imagen = f"Imagen-{random.randint(1, 1000)}"#numbrarlas
            almacen.agregar_imagen(imagen)# Agregar imagen al almacén
        time.sleep(1)  # Esperar 1 segundo antes de generar más imágenes

def max_analizar(max_robot):
    while True:
        max_robot.analizar_imagen()

if __name__ == "__main__":
    # Crear el almacén
    almacen = Almacen()

    # Crear el robot MAX
    max_robot = Max(almacen)

    # Crear hilos para generar imágenes
    hilo_generador = threading.Thread(target=generar_imagenes, args=(almacen,), daemon=True)# daemon is to terminate the thread

    # Crear 5 hilos para MAX
    hilos_max = [threading.Thread(target=max_analizar, args=(max_robot,), daemon=True) for _ in range(5)]

    # Iniciar el hilo generador
    hilo_generador.start()

    # Iniciar los hilos de MAX
    for hilo in hilos_max:
        hilo.start()

    # Mantener el programa en ejecución
    try:
        while True:
            time.sleep(1)  # Mantener el hilo principal activo
    except KeyboardInterrupt:
        print("\n[!] Programa terminado.")