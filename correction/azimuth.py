def normalize_angle(angle):
    # 角度を-180から180の範囲に正規化
    while angle > 180:
        angle -= 360
    while angle < -180:
        angle += 360
    return angle

def azimuth(mag_x, mag_y, index):
    angle1 = math.atan2(mag_y[index-1], mag_x[index-1]) # 前の角度
    angle2 = math.atan2(mag_y[index], mag_x[index]) # 現在の角度
    angle_change = normalize_angle(math.degrees(angle2 - angle1)) # 角度の変化

    return angle_change

angleList = []
bending_angle = []
for i in range(1, len(data_mag)):
    angle_degrees = azimuth(data_mag_x, data_mag_y, i)
    angleList.append(angle_degrees)
    bending_angle.append(angle_degrees)
