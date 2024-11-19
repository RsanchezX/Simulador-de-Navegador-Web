class NodoNario:
    def _init_(self, nombre, es_archivo=False):
        self.nombre = nombre  # Nombre del archivo o carpeta
        self.hijos = []  # Lista de hijos (subdominios o archivos)
        self.es_archivo = es_archivo  # Indica si es un archivo o directorio


class ArbolNario:
    def _init_(self):
        self.raiz = NodoNario("root")  # Nodo raíz del árbol de directorios
        self.cargar_estructura()  # Carga estructura desde archivo

    # Método para agregar un nodo al árbol en la ruta especificada
    def agregar_nodo(self, ruta):
        partes = ruta.split("/")  # Divide la ruta por carpetas/subdominios
        nodo_actual = self.raiz

        for parte in partes:
            existe = next(
                (hijo for hijo in nodo_actual.hijos if hijo.nombre == parte), None
            )
            if existe:
                nodo_actual = existe  # Si existe, pasa al siguiente nodo
            else:
                nuevo_nodo = NodoNario(
                    parte, parte.endswith(".html")
                )  # Nodo archivo si termina en .html
                nodo_actual.hijos.append(nuevo_nodo)
                nodo_actual = nuevo_nodo

    # Método para listar todas las páginas en el árbol N-ario (Inorden)
    def listar_paginas(self, nodo=None):
        nodo = nodo if nodo else self.raiz
        if nodo.es_archivo:
            print(f"- {nodo.nombre}")
        for hijo in nodo.hijos:
            self.listar_paginas(hijo)

    # Cargar la estructura de host.txt
    def cargar_estructura(self):
        try:
            with open("host.txt", "r") as file:
                for linea in file:
                    ruta, _, dominio = linea.strip().split()
                    self.agregar_nodo(dominio)  # Añade el dominio a la estructura
        except FileNotFoundError:
            print("Archivo host.txt no encontrado.")
