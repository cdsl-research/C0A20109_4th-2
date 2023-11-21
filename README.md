# C0A20109_4th2

## RFIDを使用して，ESP32のセンサの起動とデータ取得
### mongo.py
- MongoDBに接続して，データの挿入と取得をするためのプログラム
#### static, templates
- web上にセンサデータを表示するためのプログラム

### rfid.py
- PCにRC-S380/Sを接続
- RFIDがタグを検知したら，server.pyが起動するプログラム

### server.py
- socket通信されたESP32に送信して，センサデータを取得するプログラム

### センサの値を使用して，マッピング補正する（correction）
#### correction/azimuth.py
- 地磁気から角度を算出するプログラム

#### correction/step_count.py
- 加速度から歩数を算出するためのプログラム

#### correction/coordinate_transformation.py
- 角度(azimuth.py)と歩数(step_count.py)と歩幅を使用して座標変換するプログラム

#### correction/map_correction.py
- 座標変換からマッピング補正するプログラム

#### correction/map.py
- 美術館の展示室を想定したマッピング
- そのマップに補正された座標を表示するプログラム
