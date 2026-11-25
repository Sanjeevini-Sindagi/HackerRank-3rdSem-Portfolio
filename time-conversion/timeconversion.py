def timeConversion(s):
    period = s[-2:]
    time = s[:-2]

    hour = int(time[:2])

    if period == "AM":
        if hour == 12:
            hour = 0

    else:
        if hour != 12:
            hour += 12

    return f"{hour:02d}" + time[2:]


# Local Test Case 1
time1 = "07:05:45PM"
print("Test Case 1:", timeConversion(time1))


# Local Test Case 2
time2 = "12:00:00AM"
print("Test Case 2:", timeConversion(time2))