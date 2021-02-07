#  Company Management System

Position = input('Please enter your position (Manager / Employee) : ')
class Manager():



    def __init__(self,name =input('Enter Your name: '),age = int(input('Enter your Age: '))):
        self.Name = name
        self.Age = age
        self.Language = []

    def Get_Name(self):
        print('Name :',self.Name)

    def Get_Age(self):
        print('Age :',self.Age)

    def Get_Language(self,Languages=list(map(str, input('Enter the languages you can speak : ').split()))):

        self.Language.extend(Languages)




class Employee(Manager):
    pass

if Position == 'Manager':
    Position = Manager()
    Position.Get_Language()
    l1=[]
    for j in Position.__dict__['Language']:
        l1.append(j)
    s1=','.join(l1)
    print('Manager',Position.Name,'can speak',s1,'language(s)')
else:
    Position = Employee()
    Position.Get_Language()
    l2=[]
    for k in Position.__dict__['Language']:
        l2.append(k)
    s2=','.join(l2)
    print('Employee', Position.Name, 'can speak', s2, 'language(s)')






