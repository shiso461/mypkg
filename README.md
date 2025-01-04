# 国際宇宙ステーションの現在位置(ISS_Position)
[![test](https://github.com/shiso461/mypkg/actions/workflows/test.yml/badge.svg)](https://github.com/shiso461/mypkg/actions/workflows/test.yml)

## 概要
- ROS 2のパッケージです
- [Open Notify API](http://api.open-notify.org/)より取得した国際宇宙ステーション(ISS)の現在位置をトピックにパブリッシュします

## ノード
- ### ISSPositionPublisher
取得したISSの現在位置を1秒ごとにnow_positionトピックにパブリッシュします．
取得する現在位置の内容は緯度(latitude)と経度(longitude)です．

## トピック
- ### now_position
ISSPositionPublisherノードからパブリッシュされた，以下の形式の情報を持ちます．
```
ISS Position: lat=<latitude>, lon=<longitude>
```


## 使用方法
ROS 2のパッケージです．各自のROS 2ワークスペースにて以下のコマンドでクローンし,その後ビルドしてください．
```
git clone https://github.com/shiso461/mypkg.git
```
実行は以下のコマンドで行えます．
```
ros2 run mypkg iss_position
```
トピックの内容は以下のコマンドで確認してください
```
ros2 topic echo now_positioin
```
```
data: 'ISS Position: lat=27.3339, lon=-24.3420'
---
data: 'ISS Position: lat=27.1947, lon=-24.2019'
---
data: 'ISS Position: lat=27.1483, lon=-24.1553'
---
```

## 注意点
listener.pyおよび，talk_listen.launch.pyはテスト用です．

## テスト済み環境
- Ubuntu 22.04 LTS ROS 2 Humble (GitHub Actions)
- Ubuntu 24.04 LTS ROS 2 Jazzy (開発環境)

## ライセンス
- このソフトウェアパッケージは，3条項BSDライセンスの下，再頒布および使用が許可されます．
- このパッケージのコードの一部は，下記のスライド（CC-BY-SA 4.0 by Ryuichi Ueda）のものを，本人の許可を得て自身の著作としたものです．
    - [ryuichiueda/slides_marp/tree/master/robosys_2024](https://github.com/ryuichiueda/slides_marp/tree/master/robosys2024)

© 2025 Soma Shirai 
