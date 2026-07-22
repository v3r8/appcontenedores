import flet as ft

def main(page: ft.Page):
    page.title = "App Contenedores"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    
    # Texto informativo en pantalla
    texto = ft.Text("App de reporte de contenedores lista", size=20)
    
    def boton_clic(e):
        texto.value = "¡Botón pulsado correctamente!"
        page.update()

    boton = ft.ElevatedButton("Hacer reporte", on_click=boton_clic)

    page.add(
        ft.Row(
            [texto, boton],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )

ft.app(target=main)
