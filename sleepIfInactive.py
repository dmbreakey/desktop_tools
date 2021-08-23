#!/usr/bin/env python3
from datetime import datetime
import desktop_tools

desktop = desktop_tools.desktop()
CANCEL_SLEEP = 0
SLEEP_DURATION = 600

working = False
ts = datetime.today()
if ts.weekday() < 5:
    if ts.hour >= 8 and ts.hour < 17:
        working = True

if working:
    desktop.setSleep(CANCEL_SLEEP)
else:
    desktop.setSleep(SLEEP_DURATION)
