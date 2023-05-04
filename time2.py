str_time = input("What time is it now?: ")
str_wait_time = input("What is the number of hours you want to wait?: ")
time = int(str_time)
wait_time = int(str_wait_time)

time_when_alarm_go_off = (time + wait_time)
print("The time when your alarm will go off will be: ", time_when_alarm_go_off)
