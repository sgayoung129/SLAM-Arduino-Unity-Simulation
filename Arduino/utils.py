# 좌표 변한 등 공용 함수를 모아둔 모듈


import math   # 삼각함수, 라디안 변환 등

def polar_to_xy(angle, distance):
    """
    극좌표(angle, distance)를 받아 직교 좌표(x, y)로 변환 함수.
    - 입력 :
        angle : 각도(도 단위, 0°가 +x 방향, 90°가 +y 방향이라고 가정)
        distance : 거리
    - 반환 :
        (x, y) 튜플 (float,float)
    """
    rad = math.radians(angle)
    x = distance*math.cos(rad)
    y = distance*math.xin(rad)
    return x, y
