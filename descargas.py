# descargas.py(modulo3)
import csv
from datetime import datetime

class ColaDescargas:
    def __init__(self):
        self.cola_descargas = []  # Cola para descargas
        self.cargar_descargas()  # Carga descargas guardadas al iniciar

    # Método para iniciar una nueva descarga
    def descargar(self, url):
        descarga = {"url": url, "fecha": datetime.now(), "estado": "Pendiente"}  # Información de la descarga
        self.cola_descargas.append(descarga)  # Añade la descarga a la cola
        print(f"Descarga iniciada: {url}")

    # Método para mostrar el estado de las descargas
    def mostrar_descargas(self):
        if not self.cola_descargas:
            print("No hay descargas.")
            return
        print("Descargas:")
        for i, descarga in enumerate(self.cola_descargas, 1):
            print(f"{i}. {descarga['url']} - {descarga['estado']} - {descarga['fecha'].strftime('%Y-%m-%d %H:%M:%S')}")

    # Método para cancelar una descarga específica
    def cancelar_descarga(self, n):
        if 0 < n <= len(self.cola_descargas):
            descarga = self.cola_descargas.pop(n - 1)  # Quita la descarga de la cola
            print(f"Descarga cancelada: {descarga['url']}")
        else:
            print("Número de descarga inválido.")

    # Método para guardar el estado de las descargas en un archivo CSV
    def guardar_descargas(self):
        with open("descargas.csv", mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["URL", "Fecha y Hora", "Estado"])
            for descarga in self.cola_descargas:
                writer.writerow([descarga['url'], descarga['fecha'].strftime('%Y-%m-%d %H:%M:%S'), descarga['estado']])
        print("Descargas guardadas en descargas.csv")

    # Método para cargar descargas desde el archivo CSV
    def cargar_descargas(self):
        try:
            with open("descargas.csv", mode="r") as file:
                reader = csv.reader(file)
                next(reader)  # Salta el encabezado
                for row in reader:
                    url, fecha, estado = row
                    fecha = datetime.strptime(fecha, '%Y-%m-%d %H:%M:%S')
                    self.cola_descargas.append({"url": url, "fecha": fecha, "estado": estado})
        except FileNotFoundError:
            print("Archivo de descargas no encontrado, comenzando con cola de descargas vacía.")
