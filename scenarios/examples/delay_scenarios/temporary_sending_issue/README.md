# コマンド
```
python3 send_dummy_event.py -s examples/delay_scenarios/temporary_sending_issue
```

# シナリオの概要
途中、イベント送信がとまり、溜まったデータが送れて一気に送られるシナリオ

# 主なポイント
**scenario.yaml** にて `delay` を使って、送信時間をコントロールしています。

# ファイル
- ~~event_template.yml~~
- [scenario.yml](./scenario.yml)