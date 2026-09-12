import flet as ft 

quests = ["Estudar Python", "Fazer exercício", "Ler 10 páginas"]

def tela_quests(page: ft.Page):
    page.title = "Arise"
    page.vertical_alignment =ft.MainAxisAlignment.CENTER
    page.horizontal_alignment= ft.CrossAxisAlignment.CENTER
    page.add(
    ft.Column (
        controls= [ft.Text(item) for item in quests ]
    ))


ft.run(tela_quests)    