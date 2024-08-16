# コマンド
```
python3 send_dummy_event.py -s examples/delay_scenarios/mixed_timestamp
```

# シナリオの概要
timestampが過去のイベントデータより、未来のイベントデータのほうが先に送られるというシナリオ

# 主なポイント
**scenario.yaml** にて `delay` を使って、送信時間をコントロールしています。

# ファイル
- ~~event_template.yml~~
- [scenario.yml](./scenario.yml)