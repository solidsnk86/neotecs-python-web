import reflex as rx
from neotecs_python_web.styles.styles import Size

class Spline(rx.Component):

    library = "@splinetool/react-spline"
    tag = "Spline"
    scene: rx.Var[
        str
    ] = "https://prod.spline.design/joLpOOYbGL-10EJ4/scene.splinecode"
    is_default = True

    lib_dependencies: list[str] = ["@splinetool/runtime"]


spline = Spline.create


def spline_3d():
    return rx.center(
        spline(),
        overflow="hidden",
        width="100%",
        height="34em",
    )



