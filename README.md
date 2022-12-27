# mypkg
ロボットシステム学2022　ros2学習リポジトリ

# ダウンロード
```
https://github.com/KodairaTakumi/mypkg.git
```

# 実行コマンド
```
ros2 launch talk_listen.launch.py
```

# 必要条件
*Ubuntu22.04
*ros2
# インストール
* Ubuntu22.04へros2のインストール方法
```
sudo apt update
sudo apt install ros-humble-desktop
```
*ワークスペースの制作
```
sudo apt install python3-colcon-common-extensions
mkdir -p ~/ros2_ws/src
cd ros2_ws/
colcon build
```
# 使い方
 * ros2をダウンロード
 * ワークスペースを制作
 * パッケージをダウンロード
 * ビルドして実行
# テスト環境
* Ubuntu22.04
# ライセンス
