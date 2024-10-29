# pestanas.py(modulo2)

class NodoPestana:
    def __init__(self, url):
        self.url = url  # URL de la pestaña
        self.prev = None  # Referencia a la pestaña anterior
        self.next = None  # Referencia a la pestaña siguiente

class ListaPestanas:
    def __init__(self):
        self.head = None  # Primer nodo de la lista (primera pestaña)
        self.current = None  # Puntero a la pestaña actual

    # Método para abrir una nueva pestaña
    def nueva_pestana(self, url):
        nueva_pestana = NodoPestana(url)  # Crear nodo para la nueva pestaña
        if not self.head:  # Si la lista está vacía
            self.head = nueva_pestana  # Asigna la nueva pestaña como el primer nodo
            self.current = nueva_pestana  # Define esta pestaña como la actual
        else:
            self.current.next = nueva_pestana  # Conecta la pestaña actual con la nueva
            nueva_pestana.prev = self.current  # Conecta la nueva pestaña con la anterior
            self.current = nueva_pestana  # Establece la nueva pestaña como la actual
        print(f"Abriste una nueva pestaña con: {url}")

    # Método para cerrar la pestaña actual
    def cerrar_pestana(self):
        if not self.current:
            print("No hay pestañas para cerrar.")
            return
        url = self.current.url  # URL de la pestaña a cerrar
        if self.current.prev:
            self.current.prev.next = self.current.next  # Salta la pestaña actual en la conexión
        if self.current.next:
            self.current.next.prev = self.current.prev
            self.current = self.current.next  # Define la siguiente pestaña como la actual
        elif self.current.prev:
            self.current = self.current.prev  # Define la anterior como la actual
        else:
            self.head = None
            self.current = None
        print(f"Cerraste la pestaña con: {url}")

    # Método para cambiar a una pestaña específica
    def cambiar_pestana(self, n):
        temp = self.head  # Empieza en la primera pestaña
        index = 1
        while temp and index < n:
            temp = temp.next  # Avanza al siguiente nodo
            index += 1
        if temp:
            self.current = temp  # Cambia la pestaña actual
            print(f"Ahora estás en la pestaña con: {temp.url}")
        else:
            print("Número de pestaña inválido.")

    # Método para mostrar todas las pestañas abiertas
    def mostrar_pestanas(self):
        temp = self.head  # Comienza desde la primera pestaña
        if not temp:
            print("No hay pestañas abiertas.")
            return
        index = 1
        print("Pestañas abiertas:")
        while temp:
            print(f"{index}. {temp.url}")  # Muestra el índice y URL de cada pestaña
            temp = temp.next
            index += 1
