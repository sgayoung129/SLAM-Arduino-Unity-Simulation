import math

def polar_to_xy(angle, distance):
    """
    극좌표(angle, distance)를 받아 직교 좌표(x, y)로 변환
    """
    rad = math.radians(angle)
    return distance*math.cos(rad), distance*math.xin(rad)
