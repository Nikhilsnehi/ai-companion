from mss import MSS, tools
import pygetwindow as gw


def capture_screen():
    window = gw.getActiveWindow()

    if window is None:
        print("No active window found.")
        return

    left = window.left
    top = window.top
    width = window.width
    height = window.height

    with MSS() as sct:
        screenshot = sct.grab({
            "left": left,
            "top": top,
            "width": width,
            "height": height
        })

        tools.to_png(
            screenshot.rgb,
            screenshot.size,
            output="screen.png"
        )

    print(f"Captured: {window.title}")