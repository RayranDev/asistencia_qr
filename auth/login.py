import flet as ft

from database.db import get_user_by_email
from auth.security import verify_password
from ui.dashboard import dashboard_view


def login_view(page: ft.Page):

    email = ft.TextField(label="Correo electrónico")
    password = ft.TextField(label="Contraseña", password=True)

    message = ft.Text(color="red")

    def login_click(e):

        user = get_user_by_email(email.value)
        print(user["password"])

        if not user:
            message.value = "Usuario no encontrado"
            page.update()
            return

        if not verify_password(password.value, user["password"]):
            message.value = "Contraseña incorrecta"
            page.update()
            return

        page.clean()
        page.add(
            dashboard_view(page, user)
        )

    return ft.Column(
        [
            ft.Text("Sistema de Asistencia QR", size=30),
            email,
            password,
            ft.ElevatedButton("Login", on_click=login_click),
            message
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )