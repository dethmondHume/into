import datetime

def create_calendar_page(month=0, year=0):
    oppo = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']
    dash = '-' * 20
    days31 = [1, 3, 5, 7, 8, 10, 12]
    days30 = [4, 6, 9, 11]
    days29_28 = [2]
    days = dash +'\nMO TU WE TH FR SA SU\n' + dash
    first_week = ''
    max_days = None
    
    if month == 0 or year == 0:
        x = datetime.datetime.today()
        year = x.year
        month = x.month
        x = datetime.datetime(year, month, 1)
        if month in days31:
            max_days = 31
        elif month in days30:
            max_days = 30
        elif month in days29_28:
            if year % 4 == 0:
                max_days = 29
            else:
                max_days = 28
    else:
        x = datetime.datetime(year, month, 1)
        if month in days31:
            max_days = 31
        elif month in days30:
            max_days = 30
        elif month in days29_28:
            if year % 4 == 0:
                max_days = 29
            else:
                max_days = 28
           
        
    start = x.weekday()
    
    for i in range(start):
        first_week = start * '000'
        if i < start:
            first_week = start * '000'
        else:
            first_week = first_week + '00'
        
            
    index = 0
    days += '\n' + first_week
    for i in range(7 - start):
        if (5 - start) == 1:
            days += oppo[i]
            index += 1
        else:
            days += oppo[i] + '0'
            index += 1
    days += '\n'
            
    for i in range(7):
        if i == 6:
            days += oppo[i]
            index += 1
        else:
            days += oppo[i] + '0'
            index += 1
    days += '\n'

    for i in range(7):
        if i == 6:
            days += oppo[i]
            index += 1
        else:
            days += oppo[index] + '0'
            index += 1
    days += '\n'

    for i in range(7):
        if i == 6:
            days += oppo[i]
            index += 1
        else:
            days += oppo[index] + '0'
            index += 1
    days += '\n'

    for i in range(7):
        if index == max_days:
            break
        if i == 6:
            days += oppo[i]
            index += 1
        else:
            days += oppo[index] + '0'
            index += 1
    if index < max_days:
        days += '\n'

    while index < max_days:
        if i == 6:
            days += oppo[i]
            index += 1
        else:
            days += oppo[index] + '0'
            index += 1
    
    
    print days
    
create_calendar_page(1, 1988)
