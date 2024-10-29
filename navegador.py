# navegador.py
import csv
from historial import Historial
from pestanas import ListaPestanas
from descargas import ColaDescargas
from web_access import WebAccess

# Inicialización de las clases de cada módulo
historial = Historial()
pestanas = ListaPestanas()
descargas = ColaDescargas()
web_access = WebAccess()

# Menú principal de la aplicación
def mostrar_menu():
    print("Bienvenido al Simulador de Navegador Web en Consola.")
    print("Comandos disponibles: ir, atras, adelante, mostrar_historial, nueva_pestana, cerrar_pestana, cambiar_pestana, mostrar_pestanas, descargar, mostrar_descargas, cancelar_descarga, listar_paginas, mostrar_contenido, guardar_historial, salir.")

# Ejecución de comandos de navegación
def ejecutar_comando(comando):
    try:
        args = comando.split()
        if args[0] == "ir":
            url = args[1]
            contenido = web_access.acceder_url(url)
            historial.visitar(url)  # Guardar en el historial
            pestanas.nueva_pestana(url)
            print(f"Contenido:\n{contenido}")
        
        elif args[0] == "atras":
            url = historial.atras()
            print(f"Regresando a: {url}")

        elif args[0] == "adelante":
            url = historial.adelante()
            print(f"Avanzando a: {url}")

        elif args[0] == "mostrar_historial":
            historial.mostrar_historial()

        elif args[0] == "nueva_pestana":
            url = args[1]
            pestanas.nueva_pestana(url)

        elif args[0] == "cerrar_pestana":
            pestanas.cerrar_pestana()

        elif args[0] == "cambiar_pestana":
            n = int(args[1])
            pestanas.cambiar_pestana(n)

        elif args[0] == "mostrar_pestanas":
            pestanas.mostrar_pestanas()

        elif args[0] == "descargar":
            url = args[1]
            descargas.descargar(url)

        elif args[0] == "mostrar_descargas":
            descargas.mostrar_descargas()

        elif args[0] == "cancelar_descarga":
            n = int(args[1])
            descargas.cancelar_descarga(n)

        elif args[0] == "listar_paginas":
            web_access.listar_paginas()

        elif args[0] == "mostrar_contenido":
            pagina = args[1]
            modo = args[2]
            contenido = web_access.mostrar_contenido(pagina, modo)
            print(f"Contenido ({modo}):\n{contenido}")

        elif args[0] == "guardar_historial":
            historial.guardar_historial()

        elif args[0] == "salir":
            historial.guardar_historial()
            descargas.guardar_descargas()
            print("Cerrando el navegador. ¡Hasta la próxima!")
            return False

        else:
            print("Comando no reconocido. Escribe 'ayuda' para ver los comandos disponibles.")
    except Exception as e:
        print(f"Error al ejecutar el comando: {e}")
    return True

# Bucle principal
def main():
    mostrar_menu()
    while True:
        comando = input("> ")
        if not ejecutar_comando(comando):
            break

if __name__ == "__main__":
    main()
