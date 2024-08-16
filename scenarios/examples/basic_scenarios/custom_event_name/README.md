# コマンド
```
python3 send_dummy_event.py -s examples/basic_scenarios/custom_event_name
```

# シナリオの概要
カスタムイベント名をデフォルト（ `DummyEvent` ）から別の名前（ `MyDummyEvent` ）に変更する

# 主なポイント
**event_template.yml** にて、 `default.eventType` に変更先のイベント名を記載

# ファイル
- [event_template.yml](./event_template.yml)
- [scenario.yml](./scenario.yml)