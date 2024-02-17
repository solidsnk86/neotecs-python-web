import reflex as rx
from neotecs_python_web.styles.fonts import Font
from neotecs_python_web.styles.styles import Size
import neotecs_python_web.styles.styles as styles

def web_info() -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.heading(
                "Acerca de NeoTecs",
                size="lg",
                font_family=Font.DEFAULT.value,
                padding_bottom="40px"
            ),
            rx.text(
                "Bienvenidos a NeoTecs, tu compañero confiable en el mundo de la tecnología inalámbrica. En NeoTecs, nos apasiona facilitar la vida digital al proporcionar soluciones eficientes y simples para la configuración de dispositivos inalámbricos."
            ),
            rx.text(
                "Quiero expresar mi agradecimiento a cada uno de nuestros usuarios. Su confianza en NeoTecs es lo que nos impulsa a mejorar continuamente y ofrecer servicios de calidad. Gracias por ser parte de nuestra comunidad."
            ),
            rx.text(
                "Tu opinión es fundamental para nosotros. Si tienes sugerencias, comentarios o alguna experiencia que deseas compartir, ¡estamos aquí para escucharte! Tu retroalimentación nos ayuda a evolucionar y a adaptarnos a tus necesidades. No dudes en compartir tus pensamientos en mi feed."
            )
        ),
        padding_y=Size.VERY_BIG.value,
        font_size=Size.DEFAULT.value,
        class_name="xl:text-start text-center"
    )