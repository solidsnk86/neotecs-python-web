import reflex as rx 

def button(text: str, url: str, color: str) -> rx.Component:
    
    return rx.link(
        rx.button(
            text,
            class_name=f"nes-btn {color}",
        ),
        href=url
    )