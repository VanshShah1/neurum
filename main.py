import flet as ft

def main(page: ft.Page):
    page.title = "browser"
    page.bgcolor = "white"

    title=ft.Text("neurum", color="black", size="100")
    prompt_field=ft.Row(controls=[ft.CupertinoTextField(placeholder_text="search...", padding=10, width=800), ft.CupertinoButton(text="search", bgcolor="black", color="white", height=40, padding=10)])
    ui=ft.Column(controls=[title, prompt_field], alignment=ft.MainAxisAlignment.CENTER)
    row=ft.ResponsiveRow(controls=[ui], alignment=ft.MainAxisAlignment.CENTER)
    page.add(row)

ft.app(main)