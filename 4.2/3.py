#!/usr/bin/env python3

import os
import sys

if len(sys.argv) > 1:
    repPath = sys.argv[1]
else:
    repPath = ""

if repPath == '':
    bash_command = ["cd C:/Users/User/Documents/GitHub/study", "git status"]
else:
    bash_command = [f"cd {repPath}", "git status"]
result_os = os.popen(' && '.join(bash_command)).read()
for result in result_os.split('\n'):
    if result.find('modified') != -1:
        prepare_result = result.replace('\tmodified:   ', (bash_command[0].split())[1])
        print(prepare_result)
