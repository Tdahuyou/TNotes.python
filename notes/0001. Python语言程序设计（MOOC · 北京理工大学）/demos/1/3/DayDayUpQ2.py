# DayDayUpQ2.py
dayfactor = 0.019
dayup = pow(1 + dayfactor, 365)
daydown = pow(1 - dayfactor, 365)
print("向上：{:.2f}，向下：{:.2f}".format(dayup, daydown))
# 向上：962.89，向下：0.00