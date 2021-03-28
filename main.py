import datetime
def enter_the_hours():
    start = input("Podaj godzinę rozpoczęcia pracy: ")
    if start == 'end':
        return 'end'
    stop = input("Podaj godzinę zakończenia pracy: ")
    if stop == 'end':
        return 'end'
    start_time = start.split(':')
    stop_time = stop.split(':')
    start_time_fin = datetime.timedelta(hours = int(start_time[0]), minutes = int(start_time[1]))
    stop_time_fin = datetime.timedelta(hours = int(stop_time[0]), minutes = int(stop_time[1]))

    return stop_time_fin - start_time_fin

overtime = ''
finished_overtime = datetime.timedelta(seconds=0)
while overtime != "end":
    print("Jeżeli chcesz zakończyć wprowadzanie, wpisz 'end'")
    overtime = enter_the_hours()
    if overtime == 'end':
        break
    elif overtime > datetime.timedelta(hours = 5, minutes = 59):
        overtime = (overtime - datetime.timedelta(hours = 8, minutes = 30))
    elif overtime > datetime.timedelta(hours=8, minutes = 59):
        overtime = (overtime - datetime.timedelta(hours = 8, minutes = 45))
    elif overtime > datetime.timedelta(hours=11, minutes = 59):
        overtime = (overtime - datetime.timedelta(hours = 9))
    finished_overtime = finished_overtime + overtime
print(f"Twoja suma nadgodzin: {finished_overtime}")
