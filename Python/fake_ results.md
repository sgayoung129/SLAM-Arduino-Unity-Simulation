## Fake Results

### OverView
본 결과는 실제 초음파 센서 입력 이전 단계에서 SLAM 파이프 라인 및 Unity 시뮬레이션 환경 검증을 위해 생성한 Fake distance data에 대한 결과를 정리 한 것이다.

fake 데이터는 이상적인 센서 환경을 가정하여 공간 설계 정보를 기반하여 수학적을 계산되었다.

---
### Environment Setting
- 공간 형태: 정사각형
- 공간 크기: 70 × 70 (cm)
- Unity 기준 크기: 0.7 × 0.7 (unit)
- 센서 위치: 공간 중앙(0,0)
- 좌표계: 2D Cartesian coordinate system
- 좌표 범위: x, y ∈ [-0.35, 0.35]

센서는 고정된 위치에서 360° 회전하며 각 각도에서 가장 가까운 벽까지의 거리를 측정한다고 가정하였다.

---
### Fake Data Generation
- 생성 스크립트: `Python/fake_data.py`
- 출력 파일: `fake_lidar_data.csv`
- 각도 범위: 0° ~ 355°
- 각도 해상도: 5°
- 거리 단위: meters (m)

거리 값은 센서 위치에서 해당 각도 방향으로 벽과 처음 만나는 지점까지의 직선 거리를 계산하여 생성하였다.

---
### Interpretation
본 fake 데이터는 실제 센서 노이즈, 반사 오차, 측정 지연 등이 없는 이상적인 환경을 가정한 결과로,
- 거리 계산 로직 검증
- Unity 시각화 파이프라인 테스트
- SLAM 알고리즘 입력 데이터 구조 검증
을 목적으로 사용된다.
