# シナリオサンプル

## 基本シナリオ
- [1分間に1イベント送信（5分間）](basic_scenarios/every_minute/)
- [イベント名をデフォルト（ `DummyEvent` ）から変更](./basic_scenarios/custom_event_name/)
- [同じタイミングで5回イベント送信](./basic_scenarios/multiple_events/)
- [任意の属性をイベントに付加して送信](./basic_scenarios/custom_attribute/)

## 送信遅延シナリオ
- [各イベントを10秒遅延して送信（timestampに対して10秒遅延して送信）](./delay_scenarios/all_events_delay/)
- [途中から送信が遅延するシナリオ](./delay_scenarios/temporary_sending_issue/)
- [タイムスタンプが未来のデータが先に送られるシナリオ](./delay_scenarios/mixed_timestamp/)

## テンプレート活用シナリオ
- [すべてのイベントに同一の属性/値を付加して送信](./template_scenarios/default_template/)
- [一部のイベントに対してのみ同一の属性/値を付加して送信](./template_scenarios/custom_template/)
- [テンプレートで設定した属性を一部のみ変更して送信](./template_scenarios/template_override/)

