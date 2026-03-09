import flet as ft

from database.db import create_tables
from auth.login import login_view


def main(page: ft.Page):

    page.title = "Sistema de Asistencia QR"

    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    page.add(
        login_view(page)
    )


create_tables()

ft.app(target=main)