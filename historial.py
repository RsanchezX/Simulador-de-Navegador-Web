# historial.py(modulo1)

import csv
from datetime import datetime

class Historial:
    def __init__(self):
        self.pila_historial = []  # Pila principal de páginas visitadas
        self.pila_adelante = []  # Pila secundaria para gestionar "adelante"
        self.cargar_historial()  # Carga el historial guardado al iniciar

    # Método para registrar una nueva visita
    def visitar(self, url):
        self.pila_historial.append((url, datetime.now()))  # Añade URL y fecha/hora a la pila principal
        self.pila_adelante.clear()  # Limpia la pila de adelante para reiniciar el camino de navegación
        print(f"Visitaste: {url}")  # Mensaje de confirmación

    # Método para regresar a la página anterior
    def atras(self):
        if len(self.pila_historial) > 1:  # Chequea si hay páginas para regresar
            self.pila_adelante.append(self.pila_historial.pop())  # Mueve la página actual a pila adelante
            return self.pila_historial[-1][0]  # Devuelve la URL de la nueva página actual
        print("No hay páginas anteriores.")
        return None

    # Método para avanzar a la página siguiente
    def adelante(self):
        if self.pila_adelante:  # Verifica si hay páginas en la pila de adelante
            pagina = self.pila_adelante.pop()  # Extrae la última página de la pila adelante
            self.pila_historial.append(pagina)  # Añade esa página de nuevo al historial
            return pagina[0]  # Devuelve la URL de la página restaurada
        print("No hay páginas siguientes.")
        return None

    # Método para mostrar todo el historial
    def mostrar_historial(self):
        if not self.pila_historial:  # Verifica si el historial está vacío
            print("Historial vacío.")
            return
        print("Historial de navegación:")
        for i, (url, fecha) in enumerate(self.pila_historial, 1):  # Itera sobre las páginas en el historial
            print(f"{i}. {url} - {fecha.strftime('%Y-%m-%d %H:%M:%S')}")  # Muestra el índice, URL y fecha/hora

    # Método para guardar el historial en un archivo CSV
    def guardar_historial(self):
        with open("historial.csv", mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["URL", "Fecha y Hora"])  # Escribe el encabezado
            for url, fecha in self.pila_historial:
                writer.writerow([url, fecha.strftime('%Y-%m-%d %H:%M:%S')])  # Guarda cada página en el archivo
        print("Historial guardado en historial.csv")

    # Método para cargar el historial desde el archivo CSV
    def cargar_historial(self):
        try:
            with open("historial.csv", mode="r") as file:
                reader = csv.reader(file)
                next(reader)  # Salta el encabezado
                for row in reader:
                    url, fecha = row
                    fecha = datetime.strptime(fecha, '%Y-%m-%d %H:%M:%S')
                    self.pila_historial.append((url, fecha))  # Carga cada entrada en la pila de historial
        except FileNotFoundError:
            print("Archivo de historial no encontrado, comenzando con historial vacío.")
