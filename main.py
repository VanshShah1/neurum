import flet as ft

def main(page: ft.Page):

    page.title="neurum"
    page.bgcolor="white"
    header=ft.Container(ft.Text("neurum", color="black", size=100), alignment=ft.Alignment(x=0.5, y=0.5))
    prompt_field=ft.CupertinoTextField(placeholder_text="ask neurum...", bgcolor=ft.Colors.GREY_300)
    page.add(header, prompt_field)

ft.app(main, view=ft.WEB_BROWSER)