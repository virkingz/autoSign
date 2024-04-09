#!/bin/bash
if [ ! -d "/ql/data/scripts/faker3" ]; then
    git clone  https://git.metauniverse-cn.com/https://github.com/shufflewzc/faker3.git /ql/data/scripts/faker3
else
    git -C /ql/data/scripts/faker3 reset --hard
    git -C /ql/data/scripts/faker3 pull --rebase
fi
