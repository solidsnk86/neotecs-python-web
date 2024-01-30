import reflex as rx
import neotecs_python_web.styles.styles as styles
from neotecs_python_web.styles.fonts import Font
from neotecs_python_web.components.button import button as button

def header() -> rx.Component:
    return rx.vstack(
        rx.heading(
            "Bienvenidos a NeoTecs",
            class_name="my-20",
            size="lg",
            font_family=Font.DEFAULT.value,
            text_align="center"
        ),
        rx.flex(
            rx.image(
                src="NEOTECS_LOGO_3-removebg.png",
                class_name=f"xl:w-[280px] justify-center mx-auto mt-2 w-[16em] h-[16em]"
            ),
            rx.vstack(
                rx.box(
                    rx.text(
                    "Descubre cómo configurar diferentes modelos de dispositvos inalámbricos de las marcas más conocidas con esta guía.", id="text"
                    ),
                    rx.text(
                    "Comencemos!"
                ),
                    rx.text(
                    "¿Cúal necesitas configurar hoy? Tp-Link, Ubiquiti o Mikrotik:"
                ),
                style=styles.max_width_style
                ),
                rx.flex(
                button(
                    "Tp_link",
                    color="is-success",
                    url="",
                ),
                 button(
                    "Ubiquiti",
                    color="is-primary",
                    url=""
                ),
                 button(
                    "Mikrotik",
                    color="is-error",
                    url=""
                ),
                class_name="gap-6 py-10",
                  flex_direction=["column", "column", "column", "row", "row"],
                ),
            ),
              flex_direction=["column", "column", "column", "row", "row"],
              style=styles.max_width_style
        ),
    )