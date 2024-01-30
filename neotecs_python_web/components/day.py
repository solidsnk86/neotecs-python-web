import reflex as rx
from neotecs_python_web.styles.styles import Color, Size

def day(number: int, image: str = "gift.png", url: str = "") -> rx.Component:
    return rx.box(
        rx.cond(
            url != "",
            rx.link(
                rx.image(
                    src=image,
                    alt=f"Regalo asociado al día",
                    width="85px"
                ),
                href=url,
                is_external=True,
                position="absolute"
            )
        ),
        rx.cond(
            url == "",
                rx.image(
                    src=image,
                    alt=f"Regalo asociado al día",
                    position="absolute",
                    width="85px"
                ),
        ),
        rx.text(
            number,
            padding=Size.MEDIUM.value,
            position="absolute"
        ),
        bg=Color.PRIMARY.value,
        width="100%",
        aspect_ratio="1",
        position="absolute"
    )