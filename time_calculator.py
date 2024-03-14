def add_time(start, duration,week_day=None):
  #divide start
  initial_time=start.split(' ')
  initial_hrs=initial_time[0].split(':')
  initial_hrs=int(initial_hrs[0])
  initial_min=initial_time[0].split(':')
  initial_min=int(initial_min[1])
  ampm=initial_time[1]

  #divide duration
  duration_time=duration.split(' ')
  duration_hrs=duration_time[0].split(':')
  duration_hrs=int(duration_hrs[0])
  duration_min=duration_time[0].split(':')
  duration_min=int(duration_min[1])

  #add hours
  total_hrs=initial_hrs+duration_hrs
  #print('total hrs1: ',total_hrs)
  #total minutes
  total_min=initial_min+duration_min

  #first minutes because it might add up to the final hours
  if total_min >= 60:
    total_hrs += total_min //60
    total_min %= 60

  if total_min < 10:
    total_min= str(total_min)
    total_min = "0" + total_min #This is to add up a "0" before one digit minutes


  #divide_days
  days=0
  if total_hrs>=24:
    days=total_hrs//24
    total_hrs=total_hrs%24
  #print('days: ',days)
  #print('total hrs (sobrante hrs): ',total_hrs)
  #12 hours format for the final hour
  if total_hrs>=12 and ampm=='AM':
    total_hrs-=12
    ampm='PM'
  if total_hrs>=12 and ampm=='PM':
    total_hrs-=12
    days+=1
    ampm='AM'
  if total_hrs==0:
    total_hrs=12
  #print('total_hrs: ',total_hrs)
  #days later:
  #print('days: ',days)
  if days==1:
    days_text=' (next day)'
  elif days>1:
    days_text=' ('+str(days)+' days later)'
  else:
    days_text=''
  #print(days_text)
  #week day text:
  #Weekday to upper:
  if week_day!=None:
    week_day=week_day.capitalize()
    week_days={"Monday":1,"Tuesday":2,"Wednesday":3,"Thursday":4,'Friday':5,'Saturday':6,'Sunday':7}
    #print(week_day)
    key_list=list(week_days.keys())
    val_list=list(week_days.values())
    #start week day:
    startday_number=week_days[week_day]
    #print('start day: dict value ',startday_number)
    #final day
    if days>7:
      weeks=days//7
      #print('weeks: ',weeks)
      days_module=days%7
      #print('dìas sobrantes: ',days_module)
      finalday_position=startday_number+days_module-8
    elif days >=1 and days <=7:
      finalday_position=startday_number+days-1
    else:
      finalday_position=startday_number-1
    #print('final day position: ',finalday_position)
    final_day=key_list[finalday_position]
    #print('final day: ',final_day)
    new_time= str(total_hrs)+':'+str(total_min)+' '+ampm+','+' '+final_day+days_text
  else:
    new_time= str(total_hrs)+':'+str(total_min)+' '+ampm+days_text
  return(new_time)


add_time("8:16 PM", "466:02", "tuesday")
