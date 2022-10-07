import datetime
from msilib import PID_REVNUMBER

x = datetime.datetime.now()

print(x.day, x.month, x.year, sep='-')
print(x.hour, x.strftime("%p"))
