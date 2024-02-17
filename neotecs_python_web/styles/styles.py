from enum import Enum
from .fonts import Font
from .colors import Color, TextColor

MAX_WIDTH = "1000px"

class Size(Enum):
    EXTRA_BIG = "6em"
    VERY_BIG = "4em"
    BIG = "2em"
    MEDIUM = "1.5em"
    DEFAULT = "1em"
    SMALL = "0.8em"
    VERY_SMALL = "0.5em"

STYLESHEETS = [
    "https://unpkg.com/nes.css@latest/css/nes.min.css",
    "https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap"
]

BASE_STYLE = {
    "font_family": Font.DEFAULT.value,
    "color": TextColor.PRIMARY.value,
    "background": Color.PRIMARY.value,
}

max_width_style = dict(
    align_items="start",
    padding_x=Size.BIG.value,
    width="100%",
    max_width=MAX_WIDTH,
)