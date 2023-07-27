import sys
from ParentClass import ParentClass
from MyLogger import MyLogger
from errors import DataValueError
from myData import counter, months, weekdays, findDate

def main(args):
    myStr = ' '.join(args[1:]) if len(args) > 1 else '1-ое воскресений марта'
    # myStr = '3-ое воскресение ноября'
    myArr = myStr.split(' ')
    MyLogger.configure()
    d = {'clientip': 'Task Parse Data:'}
    MyLogger.logger.info('Start work', extra = d)

    objects = []
    objects.append(type('Counter', (ParentClass,), {'mydata': counter, 'errMessage': 'Ошибка в номере', 'errData': DataValueError})())
    objects.append(type('Weekday', (ParentClass,), {'mydata': weekdays, 'errMessage': 'Ошибка в дне недели', 'errData': DataValueError})())
    objects.append(type('Month', (ParentClass,), {'mydata': months, 'errMessage': 'Ошибка в месяце', 'errData': DataValueError})())

    try:
        arr = list(map(lambda x: x[1].checkElement(myArr[x[0]]), enumerate(objects)))
        print(findDate(arr))
    except DataValueError as e:
        d = {'clientip': 'Task Parse Data:'}
        MyLogger.logger.warning(e, extra = d)
    except ValueError as e:
        d = {'clientip': 'Task Parse Data:'}
        MyLogger.logger.warning(e, extra = d)

if __name__ == '__main__':
    main(sys.argv)


