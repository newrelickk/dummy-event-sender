# コマンド
```
python3 send_dummy_event.py -s examples/template_scenarios/custom_template
```

# シナリオの概要
任意のテンプレートを使って、特定のデータのみにテンプレートから読み込んだ属性/値を追加

# 主なポイント
**event_template.yml** にて、テンプレート及び付与する属性/値を記載

**scenario.yml** にて、テンプレート名を指定

# ファイル
- [event_template.yml](./event_template.yml)
- [scenario.yml](./scenario.yml)