# コマンド
```
python3 send_dummy_event.py -s examples/basic_scenarios/every_minute
```

# シナリオの概要
1分に1回、デフォルトの内容で5分間イベントを送ります。

# 主なポイント
**scenario.yaml** にて timeの値に 0m, 1m, 2m,...と記載しており、それぞれ開始から0分後、1分後、2分後に送信されるよう記載されてます。

# ファイル
- ~~event_template.yml~~
- [scenario.yml](./scenario.yml)