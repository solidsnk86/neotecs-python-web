import reflex as rx
import neotecs_python_web.styles.styles as styles
from neotecs_python_web.styles.styles import Size
from neotecs_python_web.views.navbar import navbar as navbar
from neotecs_python_web.views.header import header as header
from neotecs_python_web.views.video_section import video_section as video_section
from neotecs_python_web.views.footer import footer as footer
from neotecs_python_web.views.web_info import web_info as web_info
from neotecs_python_web.views.tp_link import tp_link as tp_link

def index() -> rx.Component:
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
                header(),
                video_section(),
                 web_info(),
                width="100%",
                spacing=Size.VERY_BIG.value,
                style=styles.max_width_style
            )
        ),
        footer(),
    )

app = rx.App(
    stylesheets=styles.STYLESHEETS,
    style=styles.BASE_STYLE
)

meta = [
    {"name": "theme_color", "content": "#3F234D"},
    {"char_set": "UTF-8"},
    {"property": "og:url", "content": "url"},
    {"property": "og:image", "content": "favicon.png"}
]

app.add_page(
    index,
    title="NeoTecs",
    description="Configura tu CPE inalámbrico en menos de 10 minutos!",
    meta=meta
    )

@rx.page(route="/tp-link")
def tp_link():
    return rx.box(
        tp_link()
    )

app.add_page(
    tp_link,
    title="NeoTecs"
    )
