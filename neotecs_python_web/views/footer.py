import reflex as rx
from neotecs_python_web.constants import YEAR, SOLIDSNK86_URL
from neotecs_python_web.styles.styles import Size

def footer() -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.box(
                rx.vstack(
                    rx.span("El cumpleaños de solidSnk86 comienza en:"),
                    rx.text(id="countdown", class_name="text-center text-lime-400"),
                )
                ),
            rx.hstack(
                rx.flex(
                    rx.text(
                    f"© {YEAR} NeoTecs Dev · Desarrollo por", rx.link(
                    "", rx.image(src="solidsnk86.png", class_name="inline justify-center mx-auto w-24 h-24 solidsnk86"),
                    href=SOLIDSNK86_URL,
                    class_name="mx-2 hover:text-lime-400",
                    cursor="nes pointer",
                    text_decoration="none",
                    is_external=True,
                )
                )
                )
            ),
            rx.script(src="/js/countdown.js")
        ),
        class_name=f"text-zinc-600 text-[10px] transition-all w-full pt-[{Size.EXTRA_BIG.value}] border-t-2 boder-zinc-400 xl:flex flex-col"
    )