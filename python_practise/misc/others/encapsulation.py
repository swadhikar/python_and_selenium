class Car(object):
    __max_speed = 20
    __name = ''

    def __init__(self):
        self.__max_speed = 200
        self.__name = 'lamborghini'
        print("[Car.init()] Driver instance created!")

    def drive(self):
        print("[Car.init()] Driving at speed: {} ...".format(self.__max_speed))

    @property
    def speed(self):
        return self.__max_speed

    @speed.setter
    def speed(self, speed):
        assert int(speed) > 0, "Speed must be a non-zero integer"
        self.__max_speed = int(speed)

    # def __update_software(self):
    #     print("[Car.update_software()] Updating driver...")
    #     sleep(1.5)
    #     print("[Car.update_software()] Driver upto date.")


class RaceCar(Car):
    def __init__(self, name):
        super(self.__class__, self).__init__()
        self.name = name

    # @property
    # def car_name(self):
    #     return self.name
    #
    # @car_name.setter
    # def car_name(self, name):
    #     self.name = name


if __name__ == '__main__':
    my_car = RaceCar("lamborghini")
    my_car.__max_speed = "150"
    my_car.drive()

    print(my_car.speed)
    print(my_car.name)
