#!/usr/bin/python3
#encoding=utf8

from datetime import datetime, timedelta, timezone

now = datetime.now()

print(now)
# Python的timestamp是一个浮点数。如果有小数位，小数位表示毫秒数。
# 如Java和JavaScript）的timestamp使用整数表示毫秒数，
# 这种情况下只需要把timestamp除以1000就得到Python的浮点表示方法。
timestamp = now.timestamp()
print(timestamp)

# 将timestamp转换为具体时间
time = datetime.fromtimestamp(timestamp)
print(time)

# UTC时间
print(datetime.utcfromtimestamp(timestamp))

# datetime转换为str Thu--Feb 23 17:16
timeStr = now.strftime('%a--%b %d %H:%M')
print(timeStr)
timeStr = now.strftime('%Y-%m-%d %H:%M:%S')
print(timeStr)

# str 变为时间
cday = datetime.strptime(timeStr, '%Y-%m-%d %H:%M:%S')
print(cday)
print(type(cday))

# datetime加减
newTime = now + timedelta(hours=3)
print(newTime)
newTime = now - timedelta(days=1)
print(newTime)
newTime  = now + timedelta(days=2, hours=3)
print(newTime)

# 本地时间转换为UTC时间
tz_utc_8 = timezone(timedelta(hours=8))
utc8Time = now.replace(tzinfo=tz_utc_8)
print(utc8Time)

# 时区转换
utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
print(utc_dt)
bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
print(bj_dt)