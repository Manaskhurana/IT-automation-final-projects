#!/usr/bin/env python3


import os
import requests

p = {"title": "", "name": "", "date": "", "feedback": ""}
for file in os.listdir(''):
    # print(file)
    with open((os.path.join('', file))) as f:
        list_lines = []
        for line in f:
            list_lines.append(line.strip())
        # print(list_lines)
        p['title'] = list_lines[0]
        p['name'] = list_lines[1]
        p['date'] = list_lines[2]
        p['feedback'] = list_lines[3]
    # print(p)
    response = requests.post('',json=p)
    print(response.request.body)
    print(response.raise_for_status())