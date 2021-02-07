class Animals():
    def __init__(self,color,name,leg_number):
        self.Color=color
        self.Pet_Name=name
        self.LegNumber=leg_number



    def get_Legnumber(self):
        return self.LegNumber

    def get_Color(self):
        return self.Color

    def get_Type(self):
        return self.Pet_Name

    def get_info(self):
        print('{} has {} legs and it is {} color.'.format(self.Pet_Name,self.LegNumber,self.Color))

class Cat(Animals):
    def __init__(self,color,name,leg_number,skin_type):
        super().__init__(color,name,leg_number)
        self.Skin = skin_type

    def Sound_Cat(self):
        print('Meow Meow Meow')
        print('It\'s a',self.Skin,'type cat')


class Dog(Animals):
    def __init__(self,color,name,leg_number,type):
        super().__init__(color,name,leg_number)
        self.Size = type

    def Sound_Dog(self):
        print('Bow Bow Bow')

Cat1=Cat('White','Dinny',4,'Persian')

Cat1.get_info()
Cat1.Sound_Cat()

Dog1 = Dog('Brown','Puppy',4,'Bulldog')
Dog1.get_info()
Dog1.Sound_Dog()