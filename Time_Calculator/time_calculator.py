def add_time(start, duration, start_day = ""):
  new_time = ""
  #24h_hours = 0
  # If a user added a starting day, correct the input to be lower
  if start_day:
    start_day = start_day.lower()

  if start_day == 'monday':
      start_day_num = 0
  elif start_day == 'tuesday':
      start_day_num = 1
  elif start_day == 'wednesday':
      start_day_num = 2
  elif start_day == 'thursday':
      start_day_num = 3
  elif start_day == 'friday':
      start_day_num = 4
  elif start_day == 'saturday':
      start_day_num = 5
  elif start_day == 'sunday':
      start_day_num = 6
  else:
      start_day_num = -1

  #segmenting out the starting time into hours, mins and the AM or PM 
  AM_PM = start.split()[1].upper()
  start_hours = (start.split()[0]).split(':')[0]
  start_mins = (start.split()[0]).split(':')[1]

  duration_hours = duration.split(':')[0]
  duration_mins = duration.split(':')[1]
  
  mins_24h = int(start_mins) + int(duration_mins)
  # Total any multiples of 60 in the mins section over to hours, add 12 hours if we start in the PM (to convert to the 24h time) and add the duration hours
  hours_24h =  int(start_hours) + (12 * (1 if AM_PM == 'PM' else 0)) + (mins_24h//60) + int(duration_hours)

  #print("hours" + str(hours_24h))
  #after adding the excess mins to the hours, make the mins equal to only the leftover mins
  mins_24h = mins_24h%60
  #print("mins" + str(mins_24h))
  #make a days count for the "days later" section
  days_24h = hours_24h//24
  #print("mins" + str(days_24h))
  #make the hours 24h equal to the remaining hours after removing the number of days
  hours_24h = hours_24h%24
  
  #convert the 24h back into 12h display
  AM_PM_12h = ("PM" if hours_24h >= 12 else "AM")
  hours_12h = ((hours_24h - 12) if AM_PM_12h == "PM" else hours_24h)
  #account for edge case of midnight
  if hours_12h == 0:
    hours_12h += 12
  mins_12h = mins_24h

  #construct time part of new_time
  new_time = str(hours_12h) + ":" + str(mins_12h).rjust(2,"0") + " " + AM_PM_12h

  #add the days past to the day it currently is and remove the multiples of 7 from the total to get the remaining value and thus what day it currently is. convert to string.
  if start_day_num >= 0:
    end_day_num_12h = ((start_day_num + days_24h)%7)

    if end_day_num_12h == 0:
      new_time += ", " + "Monday"
    elif end_day_num_12h == 1:
      new_time += ", " + "Tuesday"
    elif end_day_num_12h == 2:
      new_time += ", " + "wednesday"
    elif end_day_num_12h == 3:
      new_time += ", " + "Thursday"
    elif end_day_num_12h == 4:
      new_time += ", " + "Friday"
    elif end_day_num_12h == 5:
      new_time += ", " + "Saturday"
    elif end_day_num_12h == 6:
      new_time += ", " + "Sunday"
      

  
  #append next day/days later information
  if days_24h == 1:
    new_time += " (next day)"
  elif days_24h > 1:
    new_time += " (" + str(days_24h) + " days later)"
   

  return new_time