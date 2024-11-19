import csv
from datetime import datetime

class NodoBusqueda:
    def _init_(self, clave, fecha):
        self.clave = clave  # Palabra clave de la búsqueda
        self.fecha = fecha  # Fecha de la búsqueda
        self.izq = None  # Subárbol izquierdo
        self.der = None  # Subárbol derecho

class HistorialBusquedaABB:
    def _init_(self):
        self.raiz = None  # Nodo raíz del ABB
        self.cargar_busquedas()  # Carga historial de archivo

    # Método para agregar una nueva búsqueda
    def agregar_busqueda(self, clave):
        fecha = datetime.now()
        self.raiz = self.insertar_busqueda(self.raiz, clave, fecha)
        print(f"Búsqueda agregada: {clave}")
        self.guardar_busquedas()

    # Inserción en ABB
    def insertar_busqueda(self, nodo, clave, fecha):
        if not nodo:
            return NodoBusqueda(clave, fecha)
        elif clave < nodo.clave:
            nodo.izq = self.insertar_busqueda(nodo.izq, clave, fecha)
        else:
            nodo.der = self.insertar_busqueda(nodo.der, clave, fecha)
        return nodo
