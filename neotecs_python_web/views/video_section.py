import reflex as rx
from neotecs_python_web.styles.fonts import Font
from neotecs_python_web.styles.colors import TextColor
from neotecs_python_web.styles.styles import Size
from neotecs_python_web.components.video_url import video_url as video_url
from neotecs_python_web.components.button import button as button
from neotecs_python_web.constants import CPE510_PC_URL, CPE510_SMARTPHONE_URL, UBIQUITI_URL

def video_section() -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.heading(
                "¿Sabés Configurar tu CPE inalámbrico?",
                size="lg",
                font_family=Font.DEFAULT.value,
                class_name="text-center my-14"
            ),
            rx.text(
                "Te dejo estos vídeos para que aprendas cómo!", class_name="py-6"
            ),
            rx.text(
                "Son guías prácticas para que puedas configurar mediante tu smartphone o cualquiera de los siguientes dispositivos:", class_name="py-6"
            ),
            rx.box(
                rx.text("Tp-Link: CPE210 - CPE220 - CPE510 - CPE605 - CPE610 - CPE710",
                class_name="bg-zinc-800 p-2 text-xs rounded text-[#92CC41]"
                ),
                rx.text("Ubiquiti: Lite Beam M5 - Grid M5 - M2 - airMAX - NanoStation M5 - M2",
                class_name="bg-zinc-800 p-2 text-xs rounded text-[#209CEE]"
                ),
                rx.text("Mikrotik: AC5 5Ghz - LHG HP5 5Ghz - STX 2.4Ghz y 5Ghz - OmniTik Series",
                class_name="bg-zinc-800 p-2 text-xs rounded text-[#E76E55]"
                ),
                 class_name="py-3"
            )
        ),
        rx.flex(
                video_url(
                url=CPE510_PC_URL
            ),           
                video_url(
                url=CPE510_SMARTPHONE_URL
            ),
                video_url(
                url=UBIQUITI_URL
            ),
            class_name="grid grid-cols-1 gap-[14px] sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-3 items-center justify-center my-8 flex-wrap"
        ),
    )