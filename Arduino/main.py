import sys, time
from data_source import get_fake_line, read_serial_line, open_serial, list_serial_ports
from utils import polar_to_xy

def main(mode='fake', port = None, vaud=9600):
    ser = None
    if mode == 'real':
        if port is None:
            ports = list_serial_ports()
            print("사용 가능한 포트:", ports)
            return
        ser = open_serial(port, baud)

try:
    while True:
        if mode == 'fake':
            line = get_fake_line()
        else:
            line = read_serial_line(ser)
        
        if not line:
            time.sleep(0.01)
            continue

        try:
            angle, distance = map(float, line.split(","))
        except:
            print("파싱 실패:", line)
            continue

        x, y = polar_to_xy(angle, distance)
        print(f"angle={angle:.1f}, dist ={distance:.2f} -> x={x:.2f}, y={y:.2f}")
        time.sleep(0.05)
    except KeyboardInterrupt:
        print("종료")
    finally:
        if ser:
            ser.close()

if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else 'fake'
    port = sys.argv[2] if len(sys.argv) > 2 else None
    main(mode, port)
