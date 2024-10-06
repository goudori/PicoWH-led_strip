import machine  # type: ignore # type: ignore
import neopixel  # type: ignore # type: ignore
import utime  # type: ignore # type: ignore
import urandom  # type: ignore

# Pin0 is the LED strip
ws = neopixel.NeoPixel(machine.Pin(0), 8)


def flowing_light():


    for i in range(7, 0, -1):
        ws[i] = ws[i - 1]
    ws[0] = (
        int(urandom.uniform(0, 255)),
        int(urandom.uniform(0, 255)),
        int(urandom.uniform(0, 255)),
    )
    ws.write()  # LEDの色を更新
    utime.sleep_ms(80)


while True:
    flowing_light()
    print(ws[0])
