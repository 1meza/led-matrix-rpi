#!/usr/bin/python3


from rgbmatrix import RGBMatrix, RGBMatrixOptions, graphics
import sys
from os import path

options = RGBMatrixOptions()
options.rows = 32
options.cols = 64
#options.chain_length = 0
#options.parallel = 0
options.hardware_mapping = 'adafruit-hat'
options.gpio_slowdown = 4

try:
    matrix = RGBMatrix(options=options)
except Exception as e:
    print(f"Error: {e}")
    sys.exit(1)

def display_text(text):
    canvas = matrix.CreateFrameCanvas()
    font = graphics.Font()
    font.LoadFont("/home/goose/led-matrix/7x13.bdf")
    textColor = graphics.Color(255, 0, 0)
    
    pos = canvas.width
    while True:
        canvas.Clear()
        len = graphics.DrawText(canvas, font, pos, 10, textColor, text)
        pos -= 1
        if (pos + len < 0):
            pos = canvas.width
        time.sleep(0.05)
        canvas = matrix.SwapOnVSync(canvas)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: sudo python3 display_text.py 'Text to display'")
        sys.exit(1)
    
    text = sys.argv[1]
    try:
        display_text(text)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
