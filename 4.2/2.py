#!/usr/bin/env python3

import os

bash_command = ["cd C:/Users/User/Documents/GitHub/study", "git status"]
result_os = os.popen(' && '.join(bash_command)).read()
for result in result_os.split('\n'):
    if result.find('modified') != -1:
        prepare_result = result.replace('\tmodified:   ', (bash_command[0].split())[1])
        print(prepare_result)
