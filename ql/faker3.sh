#!/bin/bash
#cron "10 0-23/5 * * *" script-path=faker3.sh,tag=faker3仓库更新
if [ ! -d "/ql/data/scripts/faker3" ]; then
    git clone  https://git.metauniverse-cn.com/https://github.com/shufflewzc/faker3.git /ql/data/scripts/faker3
else
    git -C /ql/data/scripts/faker3 reset --hard
    git -C /ql/data/scripts/faker3 pull --rebase
fi
