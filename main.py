import flet as ft

def main(page: ft.Page):
    # Простой интерфейс: поле ввода и вебвью
    url_input = ft.TextField(label="Введите URL", value="https://google.com")
    webview = ft.WebView(url="https://google.com", expand=True)

    def load_url(e):
        webview.url = url_input.value
        webview.update()

    page.add(
        ft.Row([url_input, ft.ElevatedButton("GO", on_click=load_url)]),
        webview
    )

ft.app(target=main)
