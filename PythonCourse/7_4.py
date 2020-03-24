import datetime

def create_calendar_page(month=0, year=0):
    date = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']
    days31 = [1, 3, 5, 7, 8, 10, 12]
    days30 = [4, 6, 9, 11]
    days29_28 = [2]
    header = '-' * 20 +'\nMO TU WE TH FR SA SU\n' + '-' * 20
    first_week = ''
    max_days = None
    index = 0
    result = ''
    
    if month == 0 or year == 0:
        x = datetime.datetime.today()
        year = x.year
        month = x.month
        x = datetime.datetime(year, month, 1)
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
    for i in range(7):
        if i < start:
            first_week = '   ' * start
        else:
            if i == 6:
                first_week += date[index]
            else:
                first_week += date[index] + ' '
            index += 1
    result = header + '\n' + first_week + '\n'

    while index < max_days:
        for i in range(7):
            if index == max_days:
                break
            if  i < 6 and index < max_days - 1:
                result += date[index] + ' '
            else:
                result += date[index]
            index += 1
        if index != max_days:
            result += '\n'
        
    return result
    
print create_calendar_page(1)
print create_calendar_page()
print create_calendar_page(3)
print create_calendar_page(04, 1992)
