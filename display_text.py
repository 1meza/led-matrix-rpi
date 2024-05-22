#!/usr/bin/python3

from rgbmatrix import RGBMatrix, RGBMatrixOptions, graphics
import sys
import time
from os import path

options = RGBMatrixOptions()
options.rows = 32
options.cols = 64
options.chain_length = 2
options.parallel = 1
options.hardware_mapping = 'adafruit-hat'
options.gpio_slowdown = 4
options.drop_privileges = False

try:
    matrix = RGBMatrix(options=options)
except Exception as e:
    print(f"Error initializing matrix: {e}")
    sys.exit(1)

def display_text(text):
    canvas = matrix.CreateFrameCanvas()
    font = graphics.Font()
    font_path = "/home/goose/rpi-rgb-led-matrix/fonts/7x14.bdf"
    
    # Debugging: Print statements to ensure correct path and existence
    print(f"Attempting to load font from: {font_path}")
    if path.exists(font_path):
        print("Font file exists.")
    else:
        print("Font file does not exist.")
        sys.exit(1)
    
    try:
        font.LoadFont(font_path)
        print("Font loaded successfully.")
    except Exception as e:
        print(f"Error loading font: {e}")
        sys.exit(1)

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
        print(f"Error in display_text: {e}")
        sys.exit(1)
