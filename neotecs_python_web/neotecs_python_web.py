import reflex as rx
import neotecs_python_web.styles.styles as styles
from neotecs_python_web.styles.styles import Size
from neotecs_python_web.views.navbar import navbar as navbar
from neotecs_python_web.views.header import header as header
from neotecs_python_web.views.video_section import video_section as video_section
from neotecs_python_web.views.footer import footer as footer
from neotecs_python_web.views.web_info import web_info as web_info
from .views.spline import spline_3d

def index() -> rx.Component:
    return rx.box(
        rx.script(src="/js/snow.js"),
        navbar(),
        spline_3d(),
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
app.add_page(
    index,
    title="NeoTecs",
    description="Configura tu CPE inalámbrico en menos de 10 minutos!",
    )
