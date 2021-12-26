#!/usr/bin/env python3
import json
import socket as s
import time as t
import datetime as dt

# set variables
i = 1
wait = 2  # интервал проверок в секундах
srv = {'drive.google.com': '0.0.0.0', 'mail.google.com': '0.0.0.0', 'google.com': '0.0.0.0'}

print('*** start script ***')
print(srv)
print('********************')

while True:
    for host in srv:
        ip = s.gethostbyname(host)
        if ip != srv[host]:
            print(str(dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")) + ' [ERROR] ' + str(host) + ' IP mistmatch: ' + srv[host] + ' ' + ip)
            srv[host] = ip
            with open(f"../4.3/{host}.json", "w") as js:
                js.write(json.dumps({host: ip}))

# счетчик итераций для отладки, закомментировать для бесконечного цикла 3 строки
    i += 1
    if i >= 50:
        break
    t.sleep(wait)