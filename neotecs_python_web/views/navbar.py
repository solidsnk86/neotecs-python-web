import reflex as rx
from neotecs_python_web.styles.styles import Size
from neotecs_python_web.components.link_icon import link_icon
from neotecs_python_web.constants import GITHUB_URL, YOUTUBE_URL

def navbar() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.image(
            src="NEOTECS_LOGO_1-removebg.png",
            width=Size.VERY_BIG.value,
            height=Size.VERY_BIG.value,
            alt="Logo de NeoTecs estilo pixelart"
        ),
        rx.text(
            "NeoTecs"
        ),
        rx.spacer(),
        link_icon(
            "github",
            url=GITHUB_URL,
        ),
        link_icon(
            "youtube",
            url=YOUTUBE_URL,
        ),
        width="100%",
        class_name="px-3",
        ),
        rx.script(src="/js/countdown.js"),
        class_name="transparent px-2 nav-switch",
    )