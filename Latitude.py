import serial
import pynmea2
import time

ser = serial.Serial("/dev/serial0", 9600, timeout=1)

print("Waiting for GPS fix (go near window/outside)...\n")

last_print = time.time()

while True:
    line = ser.readline().decode(errors="ignore").strip()

    if line.startswith("$GPGGA"):
        msg = pynmea2.parse(line)

        # print status every 2 seconds
        if time.time() - last_print > 2:
            print(f"Fix: {msg.gps_qual} | Satellites: {msg.num_sats}")
            last_print = time.time()

        if msg.gps_qual and msg.gps_qual > 0:
            print("\n? FIX ACQUIRED")
            print(f"Latitude : {msg.latitude:.6f}")
            print(f"Longitude: {msg.longitude:.6f}")
            print(f"Satellites: {msg.num_sattus}")
            print("-" * 30)
