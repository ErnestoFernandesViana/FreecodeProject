hrs_int = lambda x: int(x[:x.find(':')])
hrs_str = lambda x: x[:x.find(':')]
mins_int = lambda x: int(x[x.find(':')+1: x.find(':')+3])
mins_str = lambda x: x[x.find(':')+1: x.find(':')+3]
day_time = lambda x: x[-2:]

def convert_hrs_12to24(x:str):
    hours = hrs_int(x)
    minutes = mins_int(x)
    dtime = day_time(x)
    if dtime == 'AM':
        return f'{str(hours)}:{str(minutes)}'
    if dtime == 'PM':
        if (hours + 12) >= 24:
            raise Exception('do not exist 12 + pm')
        return f'{str(hours + 12)}:{str(minutes)}'

def convert_hrs_24to12(x:str):
    hrs = hrs_int(x)
    mins = mins_int(x)
    if hrs > 12:
        if mins < 10:
            return f'{str(hrs - 12)}:0{str(mins)} PM'
        else:
            return f'{str(hrs - 12)}:{str(mins)} PM'
    elif hrs == 12:
        if mins < 10:
            return f'{str(12)}:0{str(mins)} PM'
        else:
            return f'{str(12)}:{str(mins)} PM'
    elif hrs == 0:
        if mins < 10:
            return f'{str(12)}:0{str(mins)} AM'
        else:
            return f'{str(12)}:{str(mins)} AM'
    else:
        if mins < 10:
            return f'{str(hrs)}:0{str(mins)} AM'
        else:
            return f'{str(hrs)}:{str(mins)} AM'

def convert_to_mins(time:str):
    hrs = hrs_int(time)
    mins = mins_int(time)
    return hrs*60 + mins

convert_mins_to_days = lambda x: int(x//(24*60))

def convert_mins_to_date(x:int):
    days = x//(24*60)
    hours = x%(24*60)//60
    mins = x%60
    if mins < 10:
        return f'{str(hours)}:0{str(mins)}'
    else:
        return f'{hours}:{mins}'

def return_day(day, days_int):
    days_list = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']*2
    day = day.lower()
    day_index = days_list.index(day)
    if days_int > 7:
        days_int = days_int%7
    return days_list[day_index + days_int].title()

def add_time(start, time, day=None):

    start_24 = convert_hrs_12to24(start) #convert input time to 24 hrs format
    start_mins = convert_to_mins(start_24) #convertinput time to mins
    time_mins = convert_to_mins(time) #convert second input to mins
    summed_mins = start_mins + time_mins #sum the mins
    days_passed = convert_mins_to_days(summed_mins) #calculate the days passed
    final_date = convert_mins_to_date(summed_mins) #calculate the final time
    final_date_formated = convert_hrs_24to12(final_date) #format the final time to 12 hrs clock
    if not day:
        if days_passed == 0:
            return final_date_formated
        elif days_passed == 1:
            return f'{final_date_formated} (next day)'
        elif days_passed > 1:
            return f'{final_date_formated} ({days_passed} days later)'
    else:
        if days_passed == 0:
            return f'{final_date_formated}, {day.title()}'
        if days_passed == 1:
            return f'{final_date_formated}, {return_day(day, days_passed)} (next day)'
        if days_passed > 1:
            return f'{final_date_formated}, {return_day(day, days_passed)} ({days_passed} days later)'




if __name__ == '__main__':

    print(add_time("11:59 PM", "24:05"))
    print(add_time("2:59 AM", "24:00", "saturDay"))
