import sys, time
from data_source import get_fake_line, read_serial_line, open_serial, list_serial_ports
from utils import polar_to_xy

def main(mode='fake', port = None, baud=9600):
    """
    main 함수 : mode에 따라 fake 데이터를 생성하거나 실제 시리얼에서 데이터를 읽어 처리
    - mode : 'fake' 또는 'real'
    - prot : 실제 모드에서 사용할 포트 문자열
    - baud : 시리얼 통신 속도
    """
    ser = None   # 시리얼 객체 보관
    # real 모드이면 ptserial로 포트 열기
    if mode == 'real':
        if port is None:
            ports = list_serial_ports()
            print("사용 가능한 포트:", ports)
            return
        ser = open_serial(port, baud)

try:
    # 무한 루프 : 데이터 취득 -> 파싱 -> 좌표 변환 -> 출
    while True:
        # 데이터 소스 선택: fake 모드면 내부 함수로 라인 생성, real이면 시리얼에서 읽음
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
            # 파싱 실패 시 원본 라인을 출력하고 루프 계속
            print("파싱 실패:", line)
            continue
            
        # 극좌표 -> 직교좌표 변환 (utils 모듈 사용)
        x, y = polar_to_xy(angle, distance)
        print(f"angle={angle:.1f}, dist ={distance:.2f} -> x={x:.2f}, y={y:.2f}")
        time.sleep(0.05)
    except KeyboardInterrupt:
        print("종료")
    finally:
        if ser:
            ser.close()

# 스크립트 직접 실행 시 커맨드라인 인자에서 모드, 포트 받아서 main 호출
if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else 'fake'
    port = sys.argv[2] if len(sys.argv) > 2 else None
    main(mode, port)
