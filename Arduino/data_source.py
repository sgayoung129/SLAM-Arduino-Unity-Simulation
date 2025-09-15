# 데이터 소스를 모아둔 모듈 (가짜 데이터 생성, 시리얼 입출력 관련)
# 이 파일을 통해  fake 데이터 생성과 실제 시리얼 포트 열기/읽기를 분리하여 관리


import random, math, time

try:
    import serial
    from serial.tools import list_ports
except:
    serial = None
# pyserial이 없을 때는 None으로 두어나중에 실제 모드 실행 시 체크 가능.

def list_serial_ports():
    """
    사용 가능한 시리얼 포트 목록을 반환. - pyseerial이 설치되지 않았거나 권한 문제일 경우 빈 리스트 반환   
    """
    if serial is None:
        return []    # 빈 리스트 반환
    return [p.device for p in list_ports.comports()]   # list_ports.comports()는 시스템의 포트 정보를 담은 generator/리스트 반환 

def get_fake_line():
    """
    fake 센서 데이터 한 줄을 생성하여 문자열로 반환
    포맷 : "각도, 거리"
    angle : 0~180 (정수)
    distance : 10.00~100.00 (소수 2자리)
    """
    angle = random.randint(0, 180)
    distance = round(random.uniform(10, 100), 2)
    return f"{angle},{distance}"

def read_serial_line(ser):
    """
    열린 serial.Serial 객체(ser)에서 한 줄 읽어 디코딩하여 반환
    - ser.readline()은 바이트열을 반환 -> decode()로 문자열로 변환
    - errors='ignore'로 디코딩 오류가 있으면 문제 바이트 무시
    - strip()으로 앞뒤 공백/개행 제거 
    """
    # timeout이 설정되어 있으면 빈 문자열을 반환할 수도 있으니 호출 측에서 체크 필요
    line = ser.readline().decode(errors='ignore').strip()
    return line

def open_serial(port, baud=9600):
    """
    주어진 포트(port)와 baud로 시리얼 포트를열어 Serial 객체를 반환
    - pyserial 미설치 시 ImportError 발생
    - timeout : 읽기 동작에서 블로킹을 막기 위한 timeout(초)
    """
    if serial is None:
        # 실제 환경에서 이 함수를 호출할 때는 반드시 pyserial이 설치되어 있어야 함.
        raise ImportError("pyserial이 설치되어 있지 않습니다.")
    # Serial 객체를 생성하여 반환 (호출자가 close()를 관리) 
    return serial.Serial(port, baud, timeout=1)
