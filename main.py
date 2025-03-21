import flet as ft

def main(page: ft.Page):
    page.title = "neurum"
    page.bgcolor = "white"

    title=ft.Container(ft.Text('neurum', color="black", size=80), padding=ft.Padding(left=500, right= 100, top=100, bottom=100))

    page.add(title)

ft.app(main)