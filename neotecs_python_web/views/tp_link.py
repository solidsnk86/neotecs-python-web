import reflex as rx
from neotecs_python_web.views.footer import footer as footer

def tp_link() -> rx.Component:
    return rx.box(
        rx.vstack(

        ),
        footer()
    )