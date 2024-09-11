'''
	args(non-keyword arguments) and kwargs(key-word argument(passed data to/from a module))
'''
from os import system

student={
    'idno':'0001',
    'lastname':'durano',
    'firstname':'dennis',
    'course':'bscpe',
    'level':'3',
}

def showmessage(*message)->None:
    [print(f"{msg}",end=" ") for msg in message]
    
    print(f"\n@index:2 {message[2]}")
    
def showstudent(student:dict)->None:
    for key,value in student.items():
        print(f"{key} : {value} ")

def showst(**student)->None:
    for key,value in student.items():
        print(f"{key} : {value} ")
    
def jointogether(*args,**kwargs)->None:
    showmessage(*args)
    showst(**kwargs)

def main()->None:
    system('cls')
    showmessage('hello','hello','hello','hello','hello','hello',123)
    print()
    showstudent(student)
    print()
    showst(idno='0002',lastname='alpha',firstname='bravo',course='bscs',level='2')
    print()
    showst(location='CEBU',lat='12.4358345',lng='123.754855')
    print()
    jointogether('hello',3,'world','cebu','philippines',street='osmena blvd',school_name='univesity of canteens')
    
if __name__=="__main__":
    main()
