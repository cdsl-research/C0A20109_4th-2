# 部屋のサイズ
room_width = 11
room_height = 6

# ドアの座標を定義
door1_x = 0  # ドア1のX座標
door1_y = 0  # ドア1のY座標
door2_x = 10 # ドア2のX座標
door2_y = 0  # ドア2のY座標

# ルートの座標を定義（美術館の周りを回る）
route_x = [room_width - 1, room_width - 1, 1, 1, room_width - 1, room_width - 1]  # X座標
route_y = [room_height / 2, room_height - 1, room_height - 1, 1, 1, room_height / 2]  # Y座標
route1_x = [room_width - 1+1, room_width - 1+1, 1-1, 1-1, room_width - 1+1, room_width - 1+1]  # X座標
route1_y = [room_height / 2+1, room_height - 1+1, room_height - 1+1, 1-1, 1-1, room_height / 2+1]  # Y座標
ans_x = [room_width - 1.5, room_width - 1.5, 1-1, 1-1, room_width - 1+1, room_width - 1+1]  # X座標
ans_y = [room_height / 2+1, room_height - 1+1, room_height - 1+1, 1-1, 1-1, room_height / 2+1]  # Y座標

plt.fill([0, 0, room_width, room_width], [0, room_height, room_height, 0], 'gray')
plt.fill([1, 1, room_width - 1, room_width - 1], [1, room_height - 1, room_height - 1, 1], 'lightgray')

plt.plot([door1_x, door1_x + 0.8], [door1_y, door1_y], 'brown', linewidth=10)
plt.plot([door2_x, door2_x + 1], [door2_y, door2_y], 'brown', linewidth=10)

plt.plot(route_x, route_y, 'r-', linewidth=3)
plt.plot(route1_x, route1_y, 'r-', linewidth=5)

plt.grid(True)

#plt.plot(x_coordinates_actual, y_coordinates_actual, marker='o', label='実際の座標', color='blue', markersize=10, linewidth=5)
#plt.plot(y_coordinates, x_coordinates, marker='o', label='補正前の座標', color='orange', markersize=10, linewidth=5)
#plt.plot(coordinates_x, coordinates_y, marker='o', label='補正後の座標', color='green', markersize=10, linewidth=5)

plt.legend( prop={"family":"MS Gothic"}, loc='upper left', bbox_to_anchor=(0,1.3))

plt.show()
