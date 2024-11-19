import csv
from datetime import datetime


class NodoAVL:
    def _init_(self, url, nombre, fecha):
        self.url = url  # URL del favorito
        self.nombre = nombre  # Nombre del sitio
        self.fecha = fecha  # Fecha de agregado
        self.altura = 1  # Altura del nodo para el balance del árbol
        self.izq = None  # Subárbol izquierdo
        self.der = None  # Subárbol derecho


class ArbolAVL:
    def _init_(self):
        self.raiz = None  # Nodo raíz del árbol
        self.cargar_favoritos()  # Carga favoritos guardados al iniciar

    # Método para obtener la altura de un nodo
    def obtener_altura(self, nodo):
        if not nodo:
            return 0
        return nodo.altura

    # Método para rotación a la derecha
    def rotar_derecha(self, y):
        x = y.izq
        T2 = x.der
        x.der = y
        y.izq = T2
        y.altura = 1 + max(self.obtener_altura(y.izq), self.obtener_altura(y.der))
        x.altura = 1 + max(self.obtener_altura(x.izq), self.obtener_altura(x.der))
        return x  # Nueva raíz

    # Método para rotación a la izquierda
    def rotar_izquierda(self, x):
        y = x.der
        T2 = y.izq
        y.izq = x
        x.der = T2
        x.altura = 1 + max(self.obtener_altura(x.izq), self.obtener_altura(x.der))
        y.altura = 1 + max(self.obtener_altura(y.izq), self.obtener_altura(y.der))
        return y  # Nueva raíz

    # Método para obtener el factor de balance de un nodo
    def obtener_balance(self, nodo):
        if not nodo:
            return 0
        return self.obtener_altura(nodo.izq) - self.obtener_altura(nodo.der)

    # Método para insertar un nuevo favorito en el árbol AVL
    def insertar_favorito(self, nodo, url, nombre):
        fecha = datetime.now()
        if not nodo:
            return NodoAVL(url, nombre, fecha)  # Nodo nuevo si el árbol está vacío
        elif url < nodo.url:
            nodo.izq = self.insertar_favorito(nodo.izq, url, nombre)
        elif url > nodo.url:
            nodo.der = self.insertar_favorito(nodo.der, url, nombre)
        else:
            return nodo  # URL ya existe

        nodo.altura = 1 + max(
            self.obtener_altura(nodo.izq), self.obtener_altura(nodo.der)
        )
        balance = self.obtener_balance(nodo)

        # Rotación izquierda-derecha según balance del nodo
        if balance > 1 and url < nodo.izq.url:
            return self.rotar_derecha(nodo)
        if balance < -1 and url > nodo.der.url:
            return self.rotar_izquierda(nodo)
        if balance > 1 and url > nodo.izq.url:
            nodo.izq = self.rotar_izquierda(nodo.izq)
            return self.rotar_derecha(nodo)
        if balance < -1 and url < nodo.der.url:
            nodo.der = self.rotar_derecha(nodo.der)
            return self.rotar_izquierda(nodo)

        return nodo

    # Método público para agregar favorito y guardar en archivo CSV
    def agregar_favorito(self, url, nombre):
        self.raiz = self.insertar_favorito(self.raiz, url, nombre)
        print(f"Favorito agregado: {url} - {nombre}")
        self.guardar_favoritos()

    # Método para mostrar los favoritos en postorden
    def mostrar_favoritos(self, nodo):
        if nodo:
            self.mostrar_favoritos(nodo.izq)
            self.mostrar_favoritos(nodo.der)
            print(
                f"- URL: {nodo.url}, Nombre: {nodo.nombre}, Fecha: {nodo.fecha.strftime('%Y-%m-%d %H:%M:%S')}"
            )

    # Guardar favoritos en un archivo CSV
    def guardar_favoritos(self):
        with open("favoritos.csv", mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["URL", "Nombre", "Fecha"])
            self._guardar_recursivo(self.raiz, writer)

    def _guardar_recursivo(self, nodo, writer):
        if nodo:
            writer.writerow(
                [nodo.url, nodo.nombre, nodo.fecha.strftime("%Y-%m-%d %H:%M:%S")]
            )
            self._guardar_recursivo(nodo.izq, writer)
            self._guardar_recursivo(nodo.der, writer)

    # Cargar favoritos desde un archivo CSV
    def cargar_favoritos(self):
        try:
            with open("favoritos.csv", mode="r") as file:
                reader = csv.reader(file)
                next(reader)  # Salta el encabezado
                for row in reader:
                    url, nombre, fecha_str = row
                    fecha = datetime.strptime(fecha_str, "%Y-%m-%d %H:%M:%S")
                    self.raiz = self.insertar_favorito(self.raiz, url, nombre)
        except FileNotFoundError:
            print("Archivo de favoritos no encontrado.")
