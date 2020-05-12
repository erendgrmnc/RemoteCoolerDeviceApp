from DatabaseOperator import *
import sys
from TemperatureSensor import *
from User import *


class Handler:

    def __init__(self):
        self.tempNumber = 1
        self.user = None

    def DeviceMenu(self):
        isDeviceOn = False

        print("-------SOĞUTUCU CİHAZ MENÜSÜ ------")
        print("1-) Cihazı Aç")
        print("2-) Cihazı Kapat")

        selection = input("Tercihinizi Giriniz : ")

        if selection == "1":
            isDeviceOn = True
            User = self.LoginScreen()
        elif selection == 2:
            isDeviceOn = False
            sys.exit()

    def LoginScreen(self):
        db = DatabaseOperator
        userName = input("Enter Your Username :")
        password = input("Enter Your Password : ")
        self.user = db.Login(db, userName, password)
        if self.user is not None:
            print("Welcome !")
            self.MainMenu()
            return
        else:
            print("Can't Log In !")

        return User

    def MainMenu(self):
        db = DatabaseOperator
        tmp = TemperatureSensor

        print("-------SOĞUTUCU CİHAZ ANA MENÜSÜ ------")
        print("1-) Sıcaklık Göster")
        print("2-) Cihaz Menüsüne Dön")
        selection = input("Tercihinizi Giriniz : ")

        if selection == "1":
            print("Oda Sıcaklığı  :  " + tmp.GetRandomTemp(tmp))
            db.RegisterTemperature(db, tmp.currentTemp, self.tempNumber, self.user)
            self.tempNumber += 1
            self.MainMenu()

        elif selection == "2":
            self.DeviceMenu(self)
