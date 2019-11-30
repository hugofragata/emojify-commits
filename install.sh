#!/bin/bash
wget https://raw.githubusercontent.com/hugofragata/emojify-commits/master/emojify.py -O ./.git/hooks/prepare-commit-msg
wget https://raw.githubusercontent.com/hugofragata/emojify-commits/master/emoji.json -P ./.git/hooks/
chmod +x ./.git/hooks/prepare-commit-msg
