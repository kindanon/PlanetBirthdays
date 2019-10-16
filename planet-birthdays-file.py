from datetime import timedelta, date, datetime
from itertools import chain

#POTENTIAL ORIGIN TIMES
#----------------------
#unix epoch time
#datetime(1970, 1, 1, 0, 0, 0, 0)

#harmonic convergence
#datetime(1987, 8, 16, 0, 0, 0, 0)

#prev planetary alignment
#datetime(561, 1, 1, 0, 0, 0, 0)

#earliest possible date
#datetime(1, 1, 1, 0, 0, 0, 0)

#max date before out of bounds
#datetime(9887, 12, 31, 0, 0, 0, 0)
#----------------------

#origin time, determines location of planets for a complete orbit
#since there is no real "origin location", you need to pick one
origin_date = datetime(1, 1, 1, 0, 0, 0, 0)
#show dates starting from
start_date = datetime.now()
#show dates upto
end_date = datetime(9887, 12, 31, 0, 0, 0, 0)

#storage bits
date_list=[]
orb_count = [[0,0,0,0,0,0,0,0],["Mercury :","Venus   :","Earth   :","Mars    :","Jupiter :","Saturn  :","Uranus  :","Neptune :"]]

def mercury_calc():
    #87 days 23 hours 15 minutes 44 seconds OR 87.96926 days OR 2111.262 hours
    for dates in datespan(origin_date, end_date, timedelta(hours=2111.262)):
        orb_count[0][0] += 1
        if (dates >= start_date):
            date_list.append(("Mercury " + str(orb_count[0][0]) + " " , dates.strftime("%Y-%m-%d %H:%M:%S")))

def venus_calc():
    #224 days 16 hours 49 minutes 9 seconds OR 224.7008 days OR 5392.8192 hours
    for dates in datespan(origin_date, end_date, timedelta(hours=5392.8192)):
        orb_count[0][1] += 1
        if (dates >= start_date):
            date_list.append(("Venus " + str(orb_count[0][1]) + " " , dates.strftime("%Y-%m-%d %H:%M:%S")))

def earth_calc():
    #365 days 6 hours 9 minutes 9 seconds OR 365.25636 days OR 8766.1525 hours
    date_iter = 0
    for dates in datespan(origin_date, end_date, timedelta(hours=8766.1525)):
        orb_count[0][2] += 1
        if (dates >= start_date):
            date_list.append(("Earth " + str(orb_count[0][2]) + " " , dates.strftime(str(start_date.year+date_iter).zfill(4) + "-12-31 23:59:30")))
            date_iter += 1       
    #curse-ed accuracy deficient modern calenders
    #curse-ed english language with out é
#    for dates in datespan(origin_date, end_date, timedelta(hours=8766.1525)):
#        orb_count[0][2] += 1
#        if (dates >= start_date):
#            date_list.append(("Earth " + str(orb_count[0][2]) + " " , dates.strftime("%Y-%m-%d %H:%M:%S")))

def mars_calc():
    #686 days 23 hours 30 minutes 40 seconds OR 686.97959 days OR 16487.51 hours
    for dates in datespan(origin_date, end_date, timedelta(hours=16487.51)):
        orb_count[0][3] += 1
        if (dates >= start_date):
            date_list.append(("Mars " + str(orb_count[0][3]) + " " , dates.strftime("%Y-%m-%d %H:%M:%S")))

def jupiter_calc():
    #4332 days 19 hours 41 minutes 0 seconds OR 4332.8201 days OR 103987.68 hours
    for dates in datespan(origin_date, end_date, timedelta(hours=103987.68)):
        orb_count[0][4] += 1
        if (dates >= start_date):
            date_list.append(("Jupiter " + str(orb_count[0][4]) + " " , dates.strftime("%Y-%m-%d %H:%M:%S")))

def saturn_calc():
    #10755 days 16 hours 46 minutes 0 seconds OR 10755.699 days OR 258136.77 hours
    for dates in datespan(origin_date, end_date, timedelta(hours=258136.77)):
        orb_count[0][5] += 1
        if (dates >= start_date):
            date_list.append(("Saturn " + str(orb_count[0][5]) + " " , dates.strftime("%Y-%m-%d %H:%M:%S")))

def uranus_calc():
    #30687 days 3 hours 40 minutes 0 seconds OR 30687.153 days OR 736491.67 hours
    for dates in datespan(origin_date, end_date, timedelta(hours=736491.67)):
        orb_count[0][6] += 1
        if (dates >= start_date):
            date_list.append(("Uranus " + str(orb_count[0][6]) + " " , dates.strftime("%Y-%m-%d %H:%M:%S")))

def neptune_calc():
    #NO DATA OR 60190.03 days OR 1444560.7 hours
    for dates in datespan(origin_date, end_date, timedelta(hours=1444560.7)):
        orb_count[0][7] += 1
        if (dates >= start_date):
            date_list.append(("Neptune " + str(orb_count[0][7]) + " " , dates.strftime("%Y-%m-%d %H:%M:%S")))

def datespan(startDate, endDate, delta):
    currentDate = startDate
    while currentDate < endDate:
        yield currentDate
        currentDate += delta

def main():
    mercury_calc()
    venus_calc()
    earth_calc()
    mars_calc()
    jupiter_calc()
    saturn_calc()
    uranus_calc()
    neptune_calc() 
    date_list.sort(key=lambda tup: tup[1])

    f = open('planetBirthdays.txt','w')

    for x in range(0, len(date_list)):
        f.write((date_list[x][0] + str(date_list[x][1]) + '\n'))

    #for x in range (0, len(orb_count[0])):
    #    f.write((orb_count[1][x] + ' ' + str(orb_count[0][x]) + '\n'))

if __name__=="__main__":
    main()