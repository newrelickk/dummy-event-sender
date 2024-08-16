# コマンド
```
python3 send_dummy_event.py -s examples/delay_scenarios/all_events_delay
```

# シナリオの概要
すべてのイベントがtimestampに対して30秒遅れて送信されます。

# 主なポイント
**scenario.yaml** にて `delay` に、 遅延時間（`30s`）を設定しています。

# ファイル
- ~~event_template.yml~~
- [scenario.yml](./scenario.yml)