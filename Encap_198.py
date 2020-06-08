class Car:


    __maxspeed = 0
    __name = ""

    def __init__(self):
        self.__maxspeed = 200
        self.__name = "Supercar"

    def drive(self):
##        print('driving. maxspeed ' + str(self.__name))
        print("He is driving a {} that goes {} mph.".format(self.__name,self.__maxspeed))

    def setMaxSpeed(self,speed):
        self.__maxspeed = speed


redcar = Car()
redcar.drive()
redcar.__maxspeed = 10 # Testing
redcar.setMaxSpeed(320)
redcar.drive()
