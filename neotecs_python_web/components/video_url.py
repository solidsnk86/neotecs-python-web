import reflex as rx

def video_url(url: str) -> rx.Component:
    return rx.video(
        url=url,
        width="280px",
        height="auto",
        class_name="mx-4 rounded my-10 border-2 border-[#888] video-frame",
    )