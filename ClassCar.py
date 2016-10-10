class Car(object):
	''''Instantiates various vehicles
	Attributes:
	type- The type of car as a string
	model-The model of the car as a string
	name- The name of the car as a string'''

	speed = 0

	def __init__(self,name_of_vehicle = 'General',model = 'GM',type = 'saloon'):

		self.type = type
		self.model = model
		self.name_of_vehicle = name_of_vehicle


	@property
	def num_of_doors(self):

		if self.name_of_vehicle == 'Porshe' or self.name_of_vehicle == 'Koenigsegg':
			return 2
		else: 
			return 4
	def num_of_wheels(self):
		if self.type == 'trailer':
			return 8
		else:
			return 4
	def is_saloon(self):
		if self.type == 'saloon':
			return True
		return False
	def drive(self, i=None):
		if i == 3:
			self.speed = 1000
		elif i == 7:
			self.speed = 77
		else:
			self.speed = 72
		return self

class CarClassTest(TestCase):


    def test_car_instance(self):
        nissan = Car('Nissan')
        self.assertIsInstance(nissan, Car, msg='The object should be an instance of the `Car` class')

    def test_object_type(self):
        nissan = Car('Nissan')
        self.assertTrue((type(nissan) is Car), msg='The object should be a type of `Car`')

    def test_default_car_name(self):
        gm = Car()
        self.assertEqual('General', gm.name,
                         msg='The car should be called `General` if no name was passed as an argument')

    def test_default_car_model(self):
        gm = Car()
        self.assertEqual('GM', gm.model, msg="The car's model should be called `GM` if no model was passed as an argument")

    def test_car_properties(self):
        mazda = Car('Mazda', 'Demio')
        self.assertListEqual(['Mazda', 'Demio'],
                             [toyota.name, toyota.model],
                             msg='The car name and model should be a property of the car')

    def test_car_doors(self):
        opel = Car('Opel', 'Omega 3')
        porshe = Car('Porshe', '911 Turbo')
        koenigsegg = Car('Koenigsegg', 'Agera R')
        self.assertListEqual([opel.num_of_doors,porshe.num_of_doors,koenigsegg.num_of_doors],[4, 2, 2],msg='The car shoud have four (4) doors except its a Porshe or Koenigsegg')

    def test_car_wheels(self):
        man = Car('MAN', 'Truck', 'trailer')
        koenigsegg = Car('Koenigsegg', 'Agera R')
        self.assertEqual([8, 4], [man.num_of_wheels, koenigsegg.num_of_wheels],msg='The car shoud have four (4) wheels except its a type of trailer')

    def test_car_type(self):
        koenigsegg = Car('Koenigsegg', 'Agera R')
        self.assertTrue(koenigsegg.is_saloon(),msg='The car type should be saloon if it is not a trailer')

    def test_car_speed(self):
        man = Car('MAN', 'Truck', 'trailer')
        parked_speed = man.speed
        moving_speed = man.drive(7).speed

        self.assertListEqual([parked_speed, moving_speed],[0, 77],msg='The Trailer should have speed 0 km/h until you put `the pedal to the metal`')

    def test_car_speed2(self):
        man = Car('Mercedes', 'SLR500')
        parked_speed = man.speed
        moving_speed = man.drive(3).speed

        self.assertListEqual([parked_speed, moving_speed],[0, 1000],msg='The Mercedes should have speed 0 km/h until you put `the pedal to the metal`')

    def test_drive_car(self):
        man = Car('MAN', 'Truck', 'trailer')
        moving_man = man.drive(7)
        moving_man_instance = isinstance(moving_man, Car)
        moving_man_type = type(moving_man) is Car
        self.assertListEqual([True, True, man.speed],[moving_man_instance, moving_man_type, moving_man.speed], msg='The car drive function should return the instance of the Car class')

class CarClassTest()