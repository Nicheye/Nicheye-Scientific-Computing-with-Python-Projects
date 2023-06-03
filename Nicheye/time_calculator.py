def add_time(start, duration,day=None):
  days123 = {
    "monday": 1,
    "tuesday": 2,
    "wednesday": 3,
    "thursday":4,
    "friday":5,
    "saturday":6,
    "sunday":7
  }
  days321 = {
    1: "Monday",
    2 : "Tuesday",
    3: "Wednesday",
    4:"Thursday",
    5:"Friday",
    6:"Saturday",
    7:"Sunday"
  }
  
  nextday=False
  Pmstatus = False
  someday=False
  
  #start split
  hourspoint=start.find(":")
  amorpm = start.find("PM")
  if amorpm ==-1:
    amorpm = start.find("AM")
  sign = start[amorpm:]
  sign = sign.strip()

  hours =start[:hourspoint]
  hours = hours.strip()
  hours = int(hours)
  
  minutes = start[hourspoint+1:amorpm]
  minutes.strip()
  minutes = int(minutes)
  #duration split

  hourspointdur=duration.find(":")
  hoursdur =duration[:hourspointdur]
  hoursdur = hoursdur.strip()
  hoursdur = int(hoursdur)
  minutesdur = duration[hourspointdur+1:]
  minutesdur.strip()
  minutesdur = int(minutesdur)
  
  if sign == "PM":
    hours = hours+12
  if day is not None:
    day = day.lower()
    l = days123.get(day)
    
  #func
  
  sumhours= hours+hoursdur
  summins = minutes+minutesdur
  
  if summins>=60:
    sumhours =sumhours+1
    summins =summins-60
  
    
  if 25>sumhours>12:
    sumhours = sumhours-12
    Pmstatus=True
  if sumhours==12:
    Pmstatus=True
  if 48>sumhours>24:
    sumhours = sumhours-24
    nextday=True
  if sumhours>48:
    days = sumhours/24
    days = round(days)
    sumhours = sumhours-24*days
    someday = True
    if day is not None:
      l = l+days
  if sumhours==48:
    days = sumhours/24
    days = round(days)
    sumhours = sumhours-24*days
    if sumhours==0:
      sumhours=12
    someday = True
    if day is not None:
      l = l+days

  #printing 
  
  newtime = print(sumhours,":",end="",sep="")
  if summins<10:
    newtime =print("0",summins,end="",sep="")
  else:
    newtime =print(summins,end="")
  if Pmstatus is True:
    newtime =print(" Pm ",end="")
  if Pmstatus is False:
    newtime =print(" Am ",end="")
  if nextday is True:
    newtime =print(", (nextday)",end="")
  if day is not None:
    newtime =print(days321.get(l),"",end="")
  if someday is True:
    newtime =print("({} days later)".format(days),end="")
    
  
  
    return newtime
