from mss import MSS, tools


def capture_screen():
    with MSS() as sct:
        screenshot = sct.grab(sct.monitors[1])

        tools.to_png(
            screenshot.rgb,
            screenshot.size,
            output="screen.png"
        )

    return "screen.png"