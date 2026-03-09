import flet as ft


def dashboard_view(page: ft.Page, user):

    return ft.Column(
        [
            ft.Text(f"Bienvenido {user['nombre']}"),
            ft.Text(f"Rol: {user['rol']}"),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )