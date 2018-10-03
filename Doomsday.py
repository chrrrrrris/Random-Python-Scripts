#The doomsday algorithm is a method of determining what the day is based on the date.

#need to know whether it is a leapyear for calculation.
def isLeapYear(yearToCheck):
    if yearToCheck%4 == 0 and yearToCheck%100 != 0 or yearToCheck%400 == 0:
        return(True)
    return(False)

def doomsDay(date):
    if '-' in date:
        a,b,c = date.split('-')
    if '/' in date:
        a,b,c = date.split('/')
    day = int(a)
    month = int(b)
    year = int(c)

    leapYear = isLeapYear(year)
    
    if day > 31 or day < 1:
        return("Invalid date")
    if month > 12 or month < 1:
        return("Invalid date")
    if month == 2 and day > 28 and leapYear == False:
        return("Invalid date")
    if month == 2 and day > 29:
        return("Invalid date")
    if year < 1:
        return("Invalid date")
        
    if year%400 >= 0 and year%400 < 100:
        anchorNumber = 2
    if year%400 > 99 and year%400 < 200:
        anchorNumber = 0
    if year%400 > 199 and year%400 < 300:
        anchorNumber = 5
    if year%400 > 299 and year%400 < 400:
        anchorNumber = 3
        
    lastTwoDigitsYear = int(c[-2:])
    justTwoDigits = lastTwoDigitsYear
    count = 0
    count2 = 0
    while justTwoDigits >= 0:
        justTwoDigits = justTwoDigits - 12
        if justTwoDigits >= 0:
            count+=1

    difference = lastTwoDigitsYear - (12*count)
    differenceCopy = difference

    while differenceCopy >= 0:
        differenceCopy = differenceCopy - 4
        if differenceCopy >= 0:
            count2+=1

    result = count + count2 + difference + anchorNumber

    doomsdayNumber = result%7

    if month == 1 and leapYear == False:
        compareDate = 3
    if month == 1 and leapYear == True:
        compareDate = 4
    if month == 2:
        compareDate = 28
    if month == 3:
        compareDate = 14
    if month%2 == 0 and month != 2:
        compareDate = month
    if month == 5:
        compareDate = 9
    if month == 7:
        compareDate = 11
    if month == 9:
        compareDate = 5
    if month == 11:
        compareDate = 7

    result2 = abs(day-compareDate)
    result2 = result2%7

    if compareDate > day:
        result2 = doomsdayNumber-result2
    if compareDate < day:
        result2 = doomsdayNumber+result2
    if compareDate == day:
        result2 = doomsdayNumber
        
    if result2 == -1 or 6:
        calculatedDay = "Saturday"
    if result2 == -2 or result2 == 12 or result2 == 5:
        calculatedDay = "Friday"
    if result2 == -3 or result2 == 11 or result2 == 4:
        calculatedDay = "Thursday"
    if result2 == -4 or result2 == 10 or result2 == 3:
        calculatedDay = "Wednesday"
    if result2 == -5 or result2 == 9 or result2 == 2:
        calculatedDay = "Tuesday"
    if result2 == -6 or result2 == 8 or result2 == 1:
        calculatedDay = "Monday"
    if result2 == 7 or result2 == 0:
        calculatedDay = "Sunday"
    return(calculatedDay)


