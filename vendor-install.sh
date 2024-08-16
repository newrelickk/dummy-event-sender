#!/bin/bash

if [[ -d vendor ]]; then
  rm -r vendor
fi
pip3 install -t vendor -r requirements.txt
