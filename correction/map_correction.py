import matplotlib.path as mpath
import numpy as np
# ルートの座標を定義（美術館の周りを回る）
room_width = 11  # 仮の部屋の幅
room_height = 6  # 仮の部屋の高さ

route_x = [room_width - 1, room_width - 1, 1, 1, room_width - 1, room_width - 1]  # X座標
route_y = [room_height / 2, room_height - 1, room_height - 1, 1, 1, room_height / 2]  # Y座標
route1_x = [room_width - 1+1, room_width - 1+1, 1-1, 1-1, room_width - 1+1, room_width - 1+1]  # X座標
route1_y = [room_height / 2+1, room_height - 1+1, room_height - 1+1, 1-1, 1-1, room_height / 2+1]  # Y座標

# 2つの多角形（ルート）を作成
polygon1 = mpath.Path(list(zip(route_x, route_y)))
polygon2 = mpath.Path(list(zip(route1_x, route1_y)))

# 点が多角形内にあるかどうかを確認
"""for point in coordinates1:
    print(point)
    in_polygon1 = polygon1.contains_point(point, radius=0.1)
    print(in_polygon1)
    in_polygon2 = polygon2.contains_point(point, radius=0.1)
    print(in_polygon2)

    if not in_polygon1 and in_polygon2:
        print(f"点 {point} は polygon1 の外側かつ polygon2 の内側にあります。")
    elif not in_polygon1:
        print(f"点 {point} は polygon1 の外側にのみあります。")
    elif in_polygon2:
        print(f"点 {point} は polygon2 の内側にのみあります。")
    else:
        print(f"点 {point} は上記のいずれの条件も満たしません。")"""
    # 補正された座標を格納するリスト
corrected_coordinates = []

def find_nearest_polygon_point(point, polygon_points):
    distances = [np.linalg.norm(np.array(point) - np.array(p)) for p in polygon_points]
    min_index = np.argmin(distances)
    return polygon_points[min_index]

for point in coordinates1:
    in_polygon1 = polygon1.contains_point(point, radius=0.1)
    in_polygon2 = polygon2.contains_point(point, radius=0.1)

    if not in_polygon1 and in_polygon2:
        print(f"点 {point} は polygon1 の外側かつ polygon2 の内側にあります。")
        corrected_coordinates.append(point)  # 条件を満たす場合はそのまま
    elif not in_polygon1:
        print(f"点 {point} は polygon1 の外側にのみあります。{find_nearest_polygon_point(point, list(zip(route1_x, route1_y)))}")
        corrected_coordinates.append(find_nearest_polygon_point(point, list(zip(route1_x, route1_y))))
    elif in_polygon2:
        print(f"点 {point} は polygon2 の内側にのみあります。{find_nearest_polygon_point(point, list(zip(route_x, route_y)))}")
        corrected_coordinates.append(find_nearest_polygon_point(point, list(zip(route_x, route_y))))
    else:
        corrected_coordinates.append(point)  # 条件を満たさない場合はそのまま
