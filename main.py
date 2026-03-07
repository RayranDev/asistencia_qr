import flet as ft

def main(page: ft.Page):
    page.title = "Sistema de Asistencia QR"

    page.add(
        ft.Text("Sistema de asistencia QR funcionando")
    )

ft.app(target=main, view=ft.WEB_BROWSER)