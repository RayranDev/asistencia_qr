import flet as ft
from database.db import create_tables, create_user
from auth.security import hash_password

def main(page: ft.Page):
    page.title = "Sistema de Asistencia QR"

    page.add(
        ft.Text("Sistema de asistencia QR funcionando")
    )

# Crear tablas al iniciar la app
create_tables()

# Crear admin inicial
admin_password = hash_password("admin123")

try:
    create_user(
        "Administrador",
        "admin@admin.com",
        admin_password,
        "admin"
    )
except:
    pass

ft.app(target=main)