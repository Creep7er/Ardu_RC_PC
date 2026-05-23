import serial
from pynput.keyboard import Controller, Key

def main():
    keyboard = Controller()

    # Подключение к COM-порту (укажи правильный путь, например, /dev/ttyUSB0 или /dev/ttyACM0)
    ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)

    try:
        while True:
            line = ser.readline().decode('latin1', errors='ignore').strip()
            if line:
                print(f"Received: {line}")
                if line == "IR_UP":
                    keyboard.press(Key.up)
                    keyboard.release(Key.up)
                elif line == "IR_DOWN":
                    keyboard.press(Key.down)
                    keyboard.release(Key.down)
                elif line == "IR_LEFT":
                    keyboard.press(Key.left)
                    keyboard.release(Key.left)
                elif line == "IR_RIGHT":
                    keyboard.press(Key.right)
                    keyboard.release(Key.right)
                elif line == "IR_OK":
                    keyboard.press(Key.enter)
                    keyboard.release(Key.enter)
    except KeyboardInterrupt:
        print("Exiting...")
    finally:
        ser.close()

if name == "main":
    main()
