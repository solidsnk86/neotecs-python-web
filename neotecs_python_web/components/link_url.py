import reflex as rx

def link_url(class_name: [], url: str) -> rx.Component:
    return rx.link(
        "",
        href=url,
        class_name=class_name,
        is_external=True
    )