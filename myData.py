from datetime import datetime, time, date, timedelta

year = datetime.today().year
counter = {'corr': '0', '01': 'Первый', '02': 'Второй', '03': 'Третий', '04': 'Четвертый', '05': 'Пятый', '06': 'Шестой'}
months = {'corr': '0', '01': 'Январь', '02': 'Февраль', '03': 'Март', '04': 'Апрель', '05': 'Май', '06': 'Июнь', 
                  '07': 'Июль', '08': 'Август', '09': 'Сентябрь', '10': 'Октябрь', '11': 'Ноябрь', '12': 'Декабрь'}
weekdays = {'corr': '1', '00': 'Понедельник', '01': 'Вторник', '02': 'Среда', '03': 'Четверг', '04': 'Пятница', '05': 'Суббота', 
                '06': 'Воскресение'}

# def parseDigit(self, elm):
#         return int(''.join(list(filter(str.isdigit, elm))))

def findDate(arr):
        d = date(year=year, month=arr[2], day=1)
        delta = (arr[1] - d.weekday()) if (arr[1] - d.weekday()) > 0 else 7 - abs(arr[1] - d.weekday())
        # print(d, arr[1], d.weekday())
        # print(d, d1.weekday())
        d += timedelta(days=delta)
        # print(d)
        i = 1
        while d.month == arr[2]:

            if i == arr[0]: return d
            i += 1
            d += timedelta(days=7)
        