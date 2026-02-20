import csv
import math

SPACE_HALF = 0.35  # 70cm 공간의 절반 (단위: m)

def distance_to_wall(angle_deg):
    rad = math.radians(angle_deg)
    dx = math.cos(rad)
    dy = math.sin(rad)

    t_x = SPACE_HALF / abs(dx) if dx != 0 else float('inf')
    t_y = SPACE_HALF / abs(dy) if dy != 0 else float('inf')

    return min(t_x, t_y)

with open("fake_lidar_data.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["angle", "distance"])

    for angle in range(0, 360, 5):
        dist = distance_to_wall(angle)
        writer.writerow([angle, round(dist, 3)])
