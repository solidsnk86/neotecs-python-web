import reflex as rx 

def link_icon(icon: str, url: str) -> rx.Component:
    return rx.link(
        "",
        class_name=f"nes-icon {icon} is-medium hover:shadow-lg shadow-zinc-400",
        url=url,
        is_external=True,
        cursor="pointer"
    )