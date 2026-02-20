# SLAM-Arduino-Unity-Simulation

## 프로젝트 목표
- 초음파 센서 + 서보모터를 이용해 거리 데이터를 획득
- Arduino에서 데이터를 읽고 Unity에서 시뮬레이션
- 초기 SLAM 환경 구성 및 테스트

## 하드웨어 구성
- Arduino Uno
- HC-SR04 초음파 센서
- SG90 서보모터
- 점퍼선, 브레드보드 등

### 연결 방식
- 초음파 VCC → Arduino 5V
- 초음파 GND → Arduino GND
- TRIG → D9
- ECHO → D10
- 서보 신호 → D3
- 서보 전원/그라운드 → Arduino 5V / GND
- (서보와 초음파 VCC는 브레드보드 빨간 전원라인에서 분배 가능)

## 소프트웨어 구성
- Arduino IDE (버전 2.3.7)
- Servo 라이브러리 사용
- 코드 구조:
  - `setup()`: Serial 통신 및 핀 설정
  - `loop()`: 서보 스캔 + 거리 측정 + Serial 출력

## 실험 결과
- 서보 + 초음파 센서 정상 동작
- 시리얼 모니터에서 각도와 거리 데이터 출력 확인
- 손으로 장애물 위치를 바꾸면 거리값 실시간 반영
- 서보에 초음파를 테이프로 고정하여 레이더 형태 구현

## Hardware Test
- 테스트 코드: sensor_test.ino (https://github.com/sgayoung129/SLAM-Arduino-Unity-Simulation/blob/main/Arduino/sensor_test.ino)
- 실험 날짜 및 환경 : 2026-02-08, 실내
- 초음파 센서 + 서보모터 정상 동작 확인
- 시리얼 모니터에서 각도, 거리값 출력 확인
- 손으로 장애물 위치 변경 시 거리값 실시간 반영
- 서보에 초음파를 테이프로 고정하여 레이더 형태 구현
- 배선: 
  - 초음파 VCC → Arduino 5V
  - 초음파 GND → Arduino GND
  - TRIG → D9, ECHO → D10
  - 서보 신호 → D3, 전원/그라운드 → 5V/GND
<img width="919" height="746" alt="image" src="https://github.com/user-attachments/assets/6f60d9aa-371c-4860-86d5-e1744d15fb4a" />

## space_design
- 공간 형태 : 정사각형
- 공간 크기 : 70cm × 70cm
- Unity 기준 공간 크기 : 0.7 × 0.7 (1 unit = 1m 기준)

- 좌표계 : 2D Cartesian coordinate system
- 원점(0,0)은 공간의 중앙으로 설정.
- x축 오른쪽 방향, y축 위쪽 방향
- 좌표 범위 : x, y ∈ [-0.35, 0.35] (공간 중심 기준, Unity 1 unit = 1m)

- 센서 위치 : 공간 중앙 (0,0) 고정
- 서보모터 회전에 따라 각도별 거리 측정

- 장애물:
  - 장애물 형태 : 사각형 블록
  - 장애물 크기 : 약 10cm × 15cm
  ※실제 실험 환경 구성 과정에서 장애물 크기는 일부 조정될 수 있음*
  - 장애물 배치 : 사전 정의된 위치에 고정 배치(*공간도 참고)
  
- 경계 조건:
  - 경계는 실제 물리적 장애물로 구성되어 센서 측정 시 벽을 장애물로 인식
  - 센서는 공간 외부로 이동 불가

- 공간도 : https://github.com/sgayoung129/SLAM-Arduino-Unity-Simulation/blob/main/Arduino/space_design.png

## 다음 단계
- Unity에서 레이더 데이터 시각화
- SLAM 알고리즘 시뮬레이션
- 데이터 전송 및 가상 환경에서 맵핑 테스트
