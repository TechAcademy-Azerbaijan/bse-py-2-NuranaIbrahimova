import datetime
from os.path import exists
if not exists('sample.txt'):
    with open('sample.txt', 'a') as f:
        f.write('Function name      |      worked time      |        arguments as list       |   arguments as dictionary|  function result \n')

def logger (func):

    def wrapper(*args,**kwargs):
        try:
            result=func(*args,**kwargs)
        except ZeroDivisionError as e:
            result= "ZeroDivisionError: " + str(e)
        with open("sample.txt",'a+') as f:
            if args and kwargs:
               f.write(f'{ func.__name__}    |  {str(datetime.datetime.today())}    |{str(args)}      | {str(kwargs)}     |   {str(result)}\n')
            elif args:
               f.write(f'{func.__name__}     |  {str(datetime.datetime.today())}    |{str(args)}      | {str()}           |   {str(result)}\n')
            else:
               f.write(f'{func.__name__}     |  {str(datetime.datetime.today())}    |{str()}          | {str(kwargs)}     |   {str(result)}\n')
               
    return wrapper       

@logger
def sum(a,b):
    return a+b

@logger
def divide(a,b):
    return a/b

sum(1,2)

divide(a=4,b=2)

divide(10,0)


