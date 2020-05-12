import psycopg2
from User import *


class DatabaseOperator:

    def CreateConnection(self):
        try:
            connection = psycopg2.connect(user="postgres", password="Eren1552963", host="localhost", port="5432",
                                          database="Nyat")
            return connection
        except(Exception, psycopg2.Error) as error:
            print("Error while connecting database", error)

    def Login(self, mail, password):

        connection = DatabaseOperator.CreateConnection(self)
        cursor = connection.cursor()
        command = "SELECT * FROM \"User\" WHERE \"Mail\"=" + "'" + mail + "'" + " AND  \"Password\" = " + "'" + password + "'"
        cursor.execute(command)
        userData = cursor.fetchall()
        user = User

        cursor.close()
        connection.close()

        for row in userData:
            if mail == row[0] and password == row[1]:
                user.__init__(user, row[0], row[1], row[2])
                return user
            else:
                return user

    def RegisterTemperature(self, currentTemp, tempNumber, user):
        connection = DatabaseOperator.CreateConnection(self)
        cursor = connection.cursor()
        command = "INSERT INTO \"TemperatureSensor\" (\"DeviceID\",\"Temperature\",\"TemperatureNumber\") VALUES(%s, %s, %s)"
        insertValues = (user.device_id,currentTemp,tempNumber)
        cursor.execute(command, insertValues)
        connection.commit()
        cursor.close()
        connection.close()
