import flet as ft

# Intentamos importar plyer para el GPS, con control de errores por si se ejecuta en escritorio
try:
    from plyer import gps
except ImportError:
    gps = None

class AppReporteContenedores(ft.Column):
    def __init__(self):
        super().__init__()
        self.spacing = 20
        self.padding = 20
        
        # Elementos de texto para mostrar información en pantalla
        self.txt_ubicacion = ft.Text("Ubicación GPS: No obtenida", size=14)
        self.txt_resultado = ft.Text("", size=14, italic=True)

        # Función para simular u obtener la ubicación GPS
        def obtener_ubicacion_click(e):
            if gps:
                try:
                    self.txt_ubicacion.value = "Ubicación GPS: Buscando satélites..."
                    self.update()
                except Exception as ex:
                    self.txt_ubicacion.value = f"Error GPS: {ex}"
                    self.update()
            else:
                self.txt_ubicacion.value = "Ubicación GPS: Simulada (Entorno de pruebas)"
                self.update()

        # Función para el botón de la cámara
        def tomar_foto_click(e):
            self.txt_resultado.value = "Abriendo cámara para fotografiar el contenedor..."
            self.update()

        # Función para el botón de dictado/incidencia
        def dictar_incidencia_click(e):
            self.txt_resultado.value = "Escuchando descripción de la incidencia..."
            self.update()

        # Creación de los botones adaptados a esta versión
        btn_gps = ft.Button(
            content=ft.Text("Obtener Ubicación"),
            on_click=obtener_ubicacion_click
        )

        btn_camara = ft.Button(
            content=ft.Text("Hacer Foto del Contenedor"),
            on_click=tomar_foto_click
        )

        btn_dictar = ft.Button(
            content=ft.Text("Dictar Incidencia"),
            on_click=dictar_incidencia_click
        )

        # Añadimos los controles a la columna principal
        self.controls = [
            ft.Text("Reporte de Incidencias", size=22, weight="bold"),
            ft.Divider(),
            self.txt_ubicacion,
            btn_gps,
            btn_camara,
            btn_dictar,
            self.txt_resultado,
        ]

def main(page: ft.Page):
    page.title = "App Reporte Contenedores"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.add(AppReporteContenedores())

if __name__ == "__main__":
    ft.app(target=main)