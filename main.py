import flet as ft

def main(page: ft.Page):

    page.title="neurum"
    page.bgcolor="white"
    header=ft.Text("neurum", color="black", size=100)
    prompt_field=ft.CupertinoTextField(placeholder_text="ask neurum...", bgcolor=ft.Colors.GREY_900)
    page.add(header, prompt_field)

ft.app(main)