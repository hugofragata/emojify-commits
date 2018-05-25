#!/usr/bin/env python

import sys
import json
from random import random


def emojify(c):
    file = open('emoji.json')
    d = json.load(file)
    p = c.split(' ')
    es = []
    for e in d:
        for w in p:
            if w in e['tags']:
                es.append(e['emoji'])
            if w in e['aliases']:
                es.append(e['emoji'])
    if es != []:
        for e in es:
            c += ' '+e
    else:
        c += ' '+d[int(random() * (len(d)-1))]['emoji']+' '+d[int(random() * (len(d)-1))]['emoji']
    return c


def append_to_file():
    with open(sys.argv[1], 'r') as message_file:
        lines = message_file.readlines()
        lines[0] = emojify(lines[0])
    with open(sys.argv[1], 'w') as message_file:
        message_file.write(''.join(lines).encode('utf-8'))


if __name__ == '__main__':
    append_to_file()
