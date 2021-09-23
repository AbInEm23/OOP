import problem2 as a 

Car = a.car(2018,'honda')

for i in range(5):
   Car.accelerate()
   print('The new speed after accelerating is: ', Car.get_speed())

for i in range(5):
    Car.brake()
    print('The new speed after break is: ', Car.get_speed())



