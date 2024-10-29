# web_access.py(modulo4)

import os
from bs4 import BeautifulSoup

class WebAccess:
    def __init__(self, host_file="host.txt"):
        self.host_file = host_file  # Archivo con rutas de host
        self.cargar_hosts()  # Carga los hosts al iniciar

    # Método para cargar las rutas de host desde el archivo host.txt
    def cargar_hosts(self):
        self.hosts = {}
        try:
            with open(self.host_file, "r") as file:
                for line in file:
                    ruta, ip, dominio = line.strip().split()
                    self.hosts[dominio] = ruta  # Asocia dominio con ruta de archivo
                    self.hosts[ip] = ruta  # Asocia IP con ruta de archivo
        except FileNotFoundError:
            print("Archivo de host no encontrado.")

    # Método para acceder a una URL o IP y mostrar el contenido de su archivo
    def acceder_url(self, url):
        if url in self.hosts:
            ruta = self.hosts[url]  # Obtiene la ruta del archivo correspondiente
            if os.path.exists(ruta):
                with open(ruta, "r", encoding="utf-8") as file:
                    return file.read()  # Retorna el contenido del archivo
            else:
                print("Archivo no encontrado en la ruta especificada.")
                return ""
        print("URL o IP no encontrada en el archivo de hosts.")
        return ""

    # Método para listar todas las páginas disponibles
    def listar_paginas(self):
        print("Páginas HTML disponibles:")
        for dominio, ruta in self.hosts.items():
            print(f"- {dominio} -> {ruta}")

    # Método para mostrar el contenido en modo básico o texto plano
    def mostrar_contenido(self, url, modo="basico"):
        contenido = self.acceder_url(url)
        if not contenido:
            return ""
        if modo == "texto_plano":
            soup = BeautifulSoup(contenido, "html.parser")
            return soup.get_text()  # Retorna el contenido de texto plano
        return contenido  # Retorna el contenido HTML sin procesar
