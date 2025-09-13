import random, math, time

try:
    import serial
    from serial.tools import list_ports
except:
    serial = None

def list_serial_ports():
    if seriall is None:
        return []
    return [p.device for p in list_ports.comports()]

def get_fake_line():
    angle = random.randint(0, 180)
    distance = round(random.uniform(10, 100), 2)
    return f"{angle}, {distance}"

def read_serial_line(ser):
    line = ser.readline().decode(errors='ignore').strip()
    return line

def open_serial(port, baud=9600):
    if serial is None:
        raise ImportError("ptserial이 설치되어 있지 않습니다.")
    return serial.Serial(port, baud, timeout=1)
