from datetime import datetime

class NodoBTree:
    def _init_(self, t, hoja=True):
        self.t = t  # Grado mínimo del árbol B
        self.hoja = hoja  # Define si el nodo es una hoja
        self.keys = []  # Llaves del nodo (URLs en este caso)
        self.children = []  # Hijos del nodo
        self.data = []  # Contenido en caché asociado a cada URL

class BTreeCache:
    def _init_(self, t=2):
        self.raiz = NodoBTree(t)  # Nodo raíz del árbol B
        self.t = t  # Grado mínimo del árbol B

    # Método para insertar una URL y su contenido en el árbol B
    def insertar(self, url, contenido):
        if len(self.raiz.keys) == 2 * self.t - 1:  # Si la raíz está llena
            nuevo_nodo = NodoBTree(self.t, hoja=False)  # Nodo nuevo que será la nueva raíz
            nuevo_nodo.children.append(self.raiz)
            self._dividir_hijo(nuevo_nodo, 0)  # Divide el hijo de la raíz
            self.raiz = nuevo_nodo  # Actualiza la raíz
        self._insertar_no_lleno(self.raiz, url, contenido)
        print(f"Contenido cacheado para: {url}")

    # Método privado para dividir un nodo hijo en dos cuando esté lleno
    def _dividir_hijo(self, nodo, i):
        t = self.t
        y = nodo.children[i]
        z = NodoBTree(t, y.hoja)
        nodo.children.insert(i + 1, z)
        nodo.keys.insert(i, y.keys[t - 1])
        nodo.data.insert(i, y.data[t - 1])
        z.keys = y.keys[t:(2 * t - 1)]
        z.data = y.data[t:(2 * t - 1)]
        y.keys = y.keys[0:t - 1]
        y.data = y.data[0:t - 1]
        if not y.hoja:
            z.children = y.children[t:(2 * t)]
            y.children = y.children[0:t]

    # Método privado para insertar en un nodo no lleno
    def _insertar_no_lleno(self, nodo, url, contenido):
        i = len(nodo.keys) - 1
        if nodo.hoja:
            while i >= 0 and nodo.keys[i] > url:
                i -= 1
            nodo.keys.insert(i + 1, url)
            nodo.data.insert(i + 1, (contenido, datetime.now()))
        else:
            while i >= 0 and nodo.keys[i] > url:
                i -= 1
            i += 1
            if len(nodo.children[i].keys) == 2 * self.t - 1:
                self._dividir_hijo(nodo, i)
                if nodo.keys[i] < url:
                    i += 1
            self._insertar_no_lleno(nodo.children[i], url, contenido)

    # Método para obtener el contenido de una URL en la caché
    def obtener_cache(self, url):
        contenido = self._buscar_cache(self.raiz, url)
        if contenido:
            print(f"Contenido en caché para {url}:\n{contenido[0]}")
        else:
            print(f"No se encontró {url} en la caché.")
        return contenido

    # Método privado para buscar en el árbol
    def _buscar_cache(self, nodo, url):
        i = 0
        while i < len(nodo.keys) and url > nodo.keys[i]:
            i += 1
        if i < len(nodo.keys) and nodo.keys[i] == url:
            return nodo.data[i]
        if nodo.hoja:
            return None
        return self._buscar_cache(nodo.children[i], url)

    # Método para vaciar la caché para una URL o desde una fecha específica
    def vaciar_cache(self, url=None, fecha=None):
        if url:
            self._vaciar_por_url(self.raiz, url)
            print(f"Caché vaciado para URL: {url}")
        elif fecha:
            fecha = datetime.strptime(fecha, "%Y-%m-%d")
            self._vaciar_por_fecha(self.raiz, fecha)
            print(f"Caché vaciado para entradas después de la fecha: {fecha}")

    # Método privado para vaciar caché de una URL
    def _vaciar_por_url(self, nodo, url):
        if url in nodo.keys:
            idx = nodo.keys.index(url)
            nodo.keys.pop(idx)
            nodo.data.pop(idx)
        if not nodo.hoja:
            for hijo in nodo.children:
                self._vaciar_por_url(hijo, url)

    # Método privado para vaciar caché por fecha
    def _vaciar_por_fecha(self, nodo, fecha):
        i = 0
        while i < len(nodo.data):
            if nodo.data[i][1] > fecha:
                nodo.keys.pop(i)
                nodo.data.pop(i)
            else:
                i += 1
        if not nodo.hoja:
            for hijo in nodo.children:
                self._vaciar_por_fecha(hijo, fecha)
