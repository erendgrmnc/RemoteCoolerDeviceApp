import random


class TemperatureSensor:

    def __init__(self):
        self.currentTemp = 0

    def GetRandomTemp(self):
        randomTemp = random.randint(18, 40)

        self.currentTemp = randomTemp

        returnValue = str(randomTemp) + "°C"
        return returnValue
