class Car(object):
    def __init__(self, name):
        self.__washCar()   
        self.name = name
 
    def __washCar(self):
        print 'Washing the Car'

    def fix(self):
        print 'Fixing Car...'

    def drive(self):             
        pass
 
    def breaking(self):             
        pass
 
""" Inheritance: The following class 'Inherits' from the Super Class """
class Motorcycle(Car):
    def drive(self):
        return 'Riding Bike!'
 
    def breaking(self):
        return 'Bike stopping'

""" Inheritance: The following class 'Inherits' from the Super Class """
class Sedan(Car):
    def drive(self):
        return 'The Sedan is being driven'
 
    def breaking(self):
        return 'Sedan breaking!'


""" Polymorphism is implemented below """
cars = [Sedan('Lexus'), Sedan('Shelby'), Motorcycle('Suzuki'), Motorcycle('Yamaha')]
for car in cars:
    print car.name + ': ' + car.drive()

""" The following example demonstrates Encapsulation whereby __washCar() is not accessible outside the scope of the class """
mazda = Car('Axela')
mazda.fix()
#mazda.__washCar() is not accesible from object.

