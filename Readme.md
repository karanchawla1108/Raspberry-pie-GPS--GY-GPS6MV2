# 📍 Raspberry Pi GPS Tracker (NEO-6M)

This project demonstrates how to interface a **u-blox NEO-6M GPS module** with a **Raspberry Pi** using UART serial communication.  
It reads raw NMEA sentences and extracts latitude/longitude once a valid GPS fix is acquired.

---

## Hardware Requirements

- Raspberry Pi (with GPIO header)
- NEO-6M GPS Module (GY-GPS6MV2 / Aideepen / similar)
- Ceramic GPS antenna
- Jumper wires
- Outdoor or window placement for GPS fix

---

##  Wiring (Tested & Working)

| GPS Module | Raspberry Pi Pin | GPIO |
|-----------|------------------|------|
| VCC | Pin 1 | 3.3V |
| GND | Pin 6 | GND |
| TXD | Pin 8 | GPIO14 |
| RXD | Pin 10 | GPIO15 |

>  Note: Some NEO-6M boards have TX/RX labels reversed.  
> If no data appears, swap TX and RX.

---

## ⚙️ Raspberry Pi Configuration

Enable UART and disable serial console:

```bash
sudo raspi-config
