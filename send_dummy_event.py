# -*- coding: utf-8 -*-
import logging
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), 'vendor'))

import requests
import json
import gzip
import uuid
import datetime
import yaml
import re
import time
from dotenv import load_dotenv
import argparse

load_dotenv()

CONST_ACCOUNT_ID = os.getenv('NR_ACCOUNT_ID')
CONST_LICENSE_KEY = os.getenv('NR_LICENSE_KEY')
CONST_ENDPOINT = 'https://insights-collector.newrelic.com/v1/accounts/' + CONST_ACCOUNT_ID + '/events'
CONST_EVENT_TYPE = 'DummyEvent'
CONST_DEFAULT_SCENARIO = 'default'
CONST_SCENARIOS_DIR = 'scenarios'
EVENT_TEMPLATE = 'event_template.yml'
SCENARIO_FILE = 'scenario.yml'


def post_event(event):
    print(str(event))
    body = gzip.compress(json.dumps(event).encode('utf-8'))
    headers = {'Api-Key': CONST_LICENSE_KEY,
               'Content-Encoding': 'gzip',
               'Content-Type': 'application/json'}
    r = requests.post(CONST_ENDPOINT, data=body, headers=headers)
    print(r.text)


def create_action_item(base, loop_count, event_uuid, offset, delay):
    if (delay + offset) < 0:
        raise 'Invalid time or delay. (time + delay) must be positive value.'

    data = {
        'uuid': event_uuid,
        'loopCount': loop_count,
        '_offsetTimestamp': offset,
        '_offsetSend': delay + offset,
    }
    return dict(base, **data)


def create_send_event(event, start_time):
    data = {
        'timestamp': start_time + event['_offsetTimestamp'],
        'startTime': start_time,
        'sentTimestamp': start_time + event['_offsetSend'],
    }
    d = dict(event, **data);
    # _で始まるキーは削除する
    for k in list(d.keys()):
        if k.startswith('_'):
            d.pop(k)
    return d


def convert_to_sec(delay):
    multi = {"s": 1, "m": 60, "h": 60 * 60, "d": 60 * 60 * 24}
    total = 0

    for m in multi:
        r = re.findall(r'(\d+)' + m, delay)
        if len(r) == 1:
            total += int(r[0]) * multi[m]

    if re.match(r'-(\d+d)??(\d+h)??(\d+m)??(\d+s)??', delay):
        total *= -1
    return total


def current_time():
    return datetime.datetime.now().timestamp()


def main(scenario_dir):
    with open(os.path.join(scenario_dir, SCENARIO_FILE), 'r', encoding="utf-8") as yml:
        scenario = yaml.safe_load(yml)

    try:
        with open(os.path.join(scenario_dir, EVENT_TEMPLATE), 'r', encoding="utf-8") as yml:
            templates = yaml.safe_load(yml)
    except FileNotFoundError:
        pass

    if templates is None:
        templates = {}

    default_event = {}
    if "default" in templates:
        default_event.update(templates['default'])

    if scenario is None:
        print("no data.")
        return

    event_uuid = str(uuid.uuid4())

    # load scenario
    actions = []
    for item in scenario:
        offset = convert_to_sec(item['time'])
        delay = convert_to_sec(item.get('delay', '0s'))
        loop_count = max(item.get('count', 1), 1)
        base = {
            'eventType': CONST_EVENT_TYPE,
        }
        base.update(default_event)
        if "template" in item:
            name = item['template']
            if name in templates:
                base.update(templates[name])
        if "attributes" in item:
            base.update(item['attributes'])
        actions.append(create_action_item(base, loop_count, event_uuid, offset, delay))

    # 　送信タイミング順でソートする
    actions = sorted(actions, key=lambda x: x['_offsetSend'])

    first_sleep = 60 - datetime.datetime.now().second
    print(str(first_sleep) + '秒 待機後に送信開始します。')
    time.sleep(first_sleep)

    start_time = current_time()
    sleep_offset = 0

    for item in actions:
        sleep_time = max(item['_offsetSend']*1.0 - (current_time() - start_time), 0.0)
        print(str(item['_offsetSend'] - sleep_offset) + '秒 待機します')
        # print("{:,.2f}".format(sleep_time) + '秒 待機します')

        time.sleep(sleep_time)
        sleep_offset = item['_offsetSend']
        loop_count = item['loopCount']
        for i in range(loop_count):
            post_event(create_send_event(item, int(start_time)))


parser = argparse.ArgumentParser(
                    prog='send_dummy_event.py',
                    description='ダミーイベント送信スクリプト',)

parser.add_argument('-s', dest='dir', action='store', help='シナリオフォルダ', required=False, nargs=1)
args = parser.parse_args()

target = args.dir[0] if args.dir is not None else CONST_DEFAULT_SCENARIO
main(os.path.join(CONST_SCENARIOS_DIR, target))
