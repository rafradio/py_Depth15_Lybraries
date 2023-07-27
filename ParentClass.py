from errors import DataValueError
from MyLogger import MyLogger

class ParentClass:
    mydata = {}
    errMessage = ''
    errData: DataValueError = None

    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        return instance
    
    def parseDigit(self, elm):
        res = list(filter(str.isdigit, elm))
        if res: return (True, int(''.join(res))-int(self.mydata['corr']))
        return (False, None)
    
    def findIt(self, element: str):
        elm: str = element[:3].lower().capitalize() if len(element) > 3 else element[:2].lower().capitalize()
        elm = elm + 'й' if len(element) == 3 else elm
        for key, val in self.mydata.items(): 
            if elm in val: return (True, int(key))
        return (False, None)

    def checkElement(self, elm):
        res = self.parseDigit(elm)
        if res[0]: 
            d = {'clientip': 'Task Parse Data:'}
            MyLogger.logger.info(f'{self.__class__.__name__} распарсено', extra = d)
            return res[1]
        res = self.findIt(elm)
        if res[0]: 
            d = {'clientip': 'Task Parse Data:'}
            MyLogger.logger.info(f'{self.__class__.__name__} распарсено', extra = d)
            return res[1]
        raise self.errData(self.errMessage)
        
