import flet as ft

quests = ["Estudar Python", "Fazer exercício", "Ler 10 páginas"]

def main(page: ft.Page):

    for item in quests:
        page.add(
            ft.Text(item)
            )

ft.run(main)