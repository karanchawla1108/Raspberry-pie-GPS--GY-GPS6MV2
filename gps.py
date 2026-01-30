import serial

ser = serial.Serial(
    port="/dev/serial0",   # Maps to ttyAMA0 (your UART)
    baudrate=9600,
    timeout=1
)

print("Reading GPS...")

while True:
    line = ser.readline().decode(errors="ignore").strip()
    if line.startswith("$"):
        print(line)
