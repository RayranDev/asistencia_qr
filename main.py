import flet as ft
from database.db import create_tables

def main(page: ft.Page):
    page.title = "Sistema de Asistencia QR"

    page.add(
        ft.Text("Sistema de asistencia QR funcionando")
    )

# Crear tablas al iniciar la app
create_tables()

ft.app(target=main)