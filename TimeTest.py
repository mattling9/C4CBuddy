import datetime

time = datetime.datetime.now().time()
time = time.strftime("%H:%M")

print(time)
