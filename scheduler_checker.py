import os
from datetime import datetime

timeout = 1500 # minutes
val1 = 'files' # path to files
val2 = 'configs' # path to config

default_config = []
with open(val2 + '/default.cfg', 'r') as f:
    line = f.readline()
    while line:
        default_config.append(line.strip('\n'))
        line = f.readline()

common_configs = os.listdir(val2)
common_configs.remove('default.cfg')
configs = {}
for common_config in common_configs:
    with open(val2 + '/' + common_config, 'r') as f:
        line = f.readline()
        configs[line.strip('\n').split(':')[1]] = common_config

files = os.listdir(val1)
now = datetime.now().timestamp()
for file in files:
    if file in default_config:
        last_updated = os.path.getmtime(val1 + '/' + file)
        diff_time = now - last_updated
        if diff_time < timeout * 60:
            if file in configs:
                with open(val2 + '/' + configs[file], 'r') as f:
                    line = f.readline()
                    while line:
                        line = f.readline()
                        if not line:
                            continue
                        time = line.strip('\n').split(':')[1]
                        line = f.readline()
                        sign = line.strip('\n').split(':')[1]

                        print("ВНИМАНИЕ! " + sign + " встретилась за последние " + (time if not time == '0' else str(timeout)) + " минут")
            else:
                print("WARNING! " + "file " + file + " doesn't exist in common configs!")
        else:
            print("file " + file + " has been updated " + str(int(diff_time)) + " seconds ago")
    else:
        print("WARNING! " + "file " + file + " doesn't exist in default.cfg!")
