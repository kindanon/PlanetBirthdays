from datetime import timedelta, date, datetime
from itertools import chain
#unix epoch time, used to set basis of new year
origin_date = datetime(1970, 1, 1, 0, 0, 0, 0)

#whatever date you want 
start_date = datetime(2020, 1, 1, 0, 0, 0, 0)
#whatever date you want 
end_date = datetime(2030, 1, 1, 0, 0, 0, 0)

date_list=[]

def mercury_calc():
    #87 days 23 hours 15 minutes 44 seconds
    #87.96926 days
    #2111.262 hours
    for dates in datespan(origin_date, end_date, timedelta(hours=2111.262)):
        if (dates >= start_date):
            date_list.append(("Mercury :-       : " , dates.strftime("%Y-%m-%d %H:%M:%S")))
            #print ("Mercury new year : " + dates.strftime("%Y-%m-%d %H:%M:%S"))

def venus_calc():
    #224 days 16 hours 49 minutes 9 seconds
    #224.7008 days
    #5392.8192 hours
    for dates in datespan(origin_date, end_date, timedelta(hours=5392.8192)):
        if (dates >= start_date):
            date_list.append(("Venus   : -      : " , dates.strftime("%Y-%m-%d %H:%M:%S")))
            #print ("  Venus new year : " + dates.strftime("%Y-%m-%d %H:%M:%S"))

def earth_calc():
    #365 days 6 hours 9 minutes 9 seconds
    #365.25636 days
    #8766.1525 hours
    for dates in datespan(origin_date, end_date, timedelta(hours=8766.1525)):
        if (dates >= start_date):
            date_list.append(("Earth   :  -     : " , dates.strftime("%Y-%m-%d %H:%M:%S")))
            #print ("    Earth new year : " + dates.strftime("%Y-%m-%d %H:%M:%S"))

def mars_calc():
    #686 days 23 hours 30 minutes 40 seconds
    #686.97959 days
    #16487.51 hours
    for dates in datespan(origin_date, end_date, timedelta(hours=16487.51)):
        if (dates >= start_date):
            date_list.append(("Mars    :   -    : " , dates.strftime("%Y-%m-%d %H:%M:%S")))
            #print ("      Mars new year : " + dates.strftime("%Y-%m-%d %H:%M:%S"))

def jupiter_calc():
    #4332 days 19 hours 41 minutes 0 seconds
    #4332.8201 days
    #103987.68 hours

    for dates in datespan(origin_date, end_date, timedelta(hours=103987.68)):
        if (dates >= start_date):
            date_list.append(("Jupiter :    -   : " , dates.strftime("%Y-%m-%d %H:%M:%S")))
            #print ("        Jupiter new year : " + dates.strftime("%Y-%m-%d %H:%M:%S"))

def saturn_calc():
    #10755 days 16 hours 46 minutes 0 seconds
    #10755.699 days
    #258136.77 hours
    for dates in datespan(origin_date, end_date, timedelta(hours=258136.77)):
        if (dates >= start_date):
            date_list.append(("Saturn  :     -  : " , dates.strftime("%Y-%m-%d %H:%M:%S")))
            #print ("          Saturn new year : " + dates.strftime("%Y-%m-%d %H:%M:%S"))

def uranus_calc():
    #30687 days 3 hours 40 minutes 0 seconds
    #30687.153 days
    #736491.67 hours
    for dates in datespan(origin_date, end_date, timedelta(hours=736491.67)):
        if (dates >= start_date):
            date_list.append(("Uranus  :      - : " , dates.strftime("%Y-%m-%d %H:%M:%S")))
            #print ("            Uranus new year : " + dates.strftime("%Y-%m-%d %H:%M:%S"))

def neptune_calc():
    #NO DATA
    #60190.03 days
    #1444560.7 hours
    for dates in datespan(origin_date, end_date, timedelta(hours=1444560.7)):
        if (dates >= start_date):
            date_list.append(("Neptune :       -: " , dates.strftime("%Y-%m-%d %H:%M:%S")))
            #print ("              Neptune new year : " + dates.strftime("%Y-%m-%d %H:%M:%S"))

#great solution by DzinX @ stackoverflow
def datespan(startDate, endDate, delta):
    currentDate = startDate
    while currentDate < endDate:
        yield currentDate
        currentDate += delta

def main():
#    for dates in datespan(start_date, end_date, timedelta(hours=1)):
#        print (dates)
    mercury_calc()
    venus_calc()
    earth_calc()
    mars_calc()
    jupiter_calc()
    saturn_calc()
    uranus_calc()
    neptune_calc() 
    date_list.sort(key=lambda tup: tup[1])
    for x in range(0, len(date_list)):
        print(*chain(date_list[x]))

if __name__=="__main__":
    main()