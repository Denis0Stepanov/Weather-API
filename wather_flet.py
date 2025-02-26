import flet as ft  # Импортируем библиотеку Flet
import requests 

def main(page: ft.Page):  # Главная функция, которая принимает объект страницы (интерфейса)
    page.title = "Weather"  # Устанавливаем заголовок окна
    page.theme_mode = "dark"  # Устанавливаем тёмную тему
    page.vertical_alignment = ft.MainAxisAlignment.CENTER  # Размещаем элементы по центру страницы (по вертикали)

    user_data = ft.TextField(label = "Введите город", width=400)
    wether_data = ft.Text('')
    city_name = user_data

    def get_info(e):
        if len(city_name.value) < 2:
            return

        API = '9d5f6a60e43ca7edc610d344a06f8a08'
        URL = f"https://api.openweathermap.org/data/2.5/weather?q={city_name.value}&appid={API}&units=metric"
        res = requests.get(URL).json()
        temp = res['main']['temp']
        wether_data.value = 'Погода: ' + str(temp)
        page.update()

    theme_button = ft.IconButton(
        icon=ft.icons.SUNNY,
        on_click = lambda e: change_theme(e),
    )    

    def change_theme(e):
        if page.theme_mode == 'dark':
            page.theme_mode = "light"
            theme_button.icon = ft.icons.NIGHTS_STAY
        else:
            page.theme_mode = 'dark'
            theme_button.icon = ft.icons.SUNNY
        page.update()

    page.add(
        ft.Row(
            [
                theme_button,
                ft.Text("Погодная программа")
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )
    page.add(
        ft.Row(
            [
                user_data
            ],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row([wether_data], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([ft.ElevatedButton(text='Получить', on_click=get_info)], alignment=ft.MainAxisAlignment.CENTER)
    )

ft.app(target=main)  # Запускаем приложение, передавая в него функцию main
